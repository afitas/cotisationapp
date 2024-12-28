from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Projet, ProjetBloc, CotisationProjet
from .serializers import (
    ProjetSerializer,
    ProjetBlocSerializer,
    CotisationProjetSerializer
)

class ProjetViewSet(viewsets.ModelViewSet):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def generer_cotisations(self, request, pk=None):
        projet = self.get_object()
        blocs = projet.blocs.filter(est_inclus=True)
        users = CustomUser.objects.filter(
            role='abonne',
            est_actif=True,
            bloc__in=blocs.values_list('bloc', flat=True)
        )
        
        cotisations = []
        montant_par_bloc = projet.cout_total / blocs.count()
        
        for user in users:
            cotisation = CotisationProjet.objects.create(
                projet=projet,
                user=user,
                montant_calcule=montant_par_bloc / users.count()
            )
            cotisations.append(cotisation)
            
        return Response({
            'status': 'success',
            'message': f'{len(cotisations)} cotisations générées'
        })

class ProjetBlocViewSet(viewsets.ModelViewSet):
    queryset = ProjetBloc.objects.all()
    serializer_class = ProjetBlocSerializer
    permission_classes = [permissions.IsAuthenticated]

class CotisationProjetViewSet(viewsets.ModelViewSet):
    queryset = CotisationProjet.objects.all()
    serializer_class = CotisationProjetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == 'abonne':
            return self.queryset.filter(user=self.request.user)
        return self.queryset 