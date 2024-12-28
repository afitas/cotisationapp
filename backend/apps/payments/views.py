from rest_framework import viewsets, permissions
from .models import Payment
from .serializers import PaymentSerializer, PaymentDetailSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == 'abonne':
            return self.queryset.filter(created_by=self.request.user)
        return self.queryset

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return PaymentDetailSerializer
        return PaymentSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user) 