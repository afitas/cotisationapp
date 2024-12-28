from rest_framework import serializers
from .models import AnneeAbonnement, PlanMensuel, Cotisation
from apps.users.serializers import UserSerializer

class AnneeAbonnementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnneeAbonnement
        fields = '__all__'
        read_only_fields = ['created_by', 'date_creation', 'date_cloture']

class PlanMensuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanMensuel
        fields = '__all__'
        read_only_fields = ['created_by']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['annee_display'] = str(instance.annee)
        return data

class CotisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotisation
        fields = '__all__'
        read_only_fields = ['created_by', 'date_paiement']

class CotisationDetailSerializer(CotisationSerializer):
    user = UserSerializer(read_only=True)
    plan = PlanMensuelSerializer(read_only=True)

    class Meta(CotisationSerializer.Meta):
        fields = '__all__' 