from rest_framework import serializers
from .models import Payment
from apps.subscriptions.serializers import CotisationSerializer
from apps.projects.serializers import CotisationProjetSerializer
from apps.users.serializers import UserSerializer

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ['created_by', 'date_created', 'date_updated']

class PaymentDetailSerializer(PaymentSerializer):
    cotisation = CotisationSerializer(read_only=True)
    cotisation_projet = CotisationProjetSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta(PaymentSerializer.Meta):
        fields = '__all__' 