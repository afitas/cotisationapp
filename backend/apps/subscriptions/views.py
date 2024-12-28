from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import AnneeAbonnement, PlanMensuel, Cotisation
from .serializers import (
    AnneeAbonnementSerializer,
    PlanMensuelSerializer,
    CotisationSerializer,
    CotisationDetailSerializer
)

class AnneeAbonnementViewSet(viewsets.ModelViewSet):
    queryset = AnneeAbonnement.objects.all()
    serializer_class = AnneeAbonnementSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['post'])
    def cloturer(self, request, pk=None):
        annee = self.get_object()
        annee.cloturer_annee()
        return Response({'status': 'année clôturée'})

class PlanMensuelViewSet(viewsets.ModelViewSet):
    queryset = PlanMensuel.objects.all()
    serializer_class = PlanMensuelSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['post'])
    def generer_cotisations(self, request, pk=None):
        plan = self.get_object()
        users = CustomUser.objects.filter(role='abonne', est_actif=True)
        cotisations_created = []

        for user in users:
            cotisation = Cotisation.objects.create(
                user=user,
                plan=plan,
                montant_total=plan.calculer_montant(user.nombre_voitures),
                created_by=request.user
            )
            cotisations_created.append(cotisation)

        return Response({
            'status': 'success',
            'message': f'{len(cotisations_created)} cotisations générées'
        })

class CotisationViewSet(viewsets.ModelViewSet):
    queryset = Cotisation.objects.all()
    serializer_class = CotisationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == 'abonne':
            return self.queryset.filter(user=self.request.user)
        return self.queryset

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return CotisationDetailSerializer
        return CotisationSerializer

    @action(detail=True, methods=['post'])
    def marquer_payee(self, request, pk=None):
        cotisation = self.get_object()
        cotisation.statut = 'paye'
        cotisation.date_paiement = timezone.now()
        cotisation.save()
        return Response({'status': 'cotisation marquée comme payée'}) 