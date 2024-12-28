from rest_framework import serializers
from .models import Projet, ProjetBloc, CotisationProjet
from apps.announcements.serializers import AnnonceSerializer
from apps.users.serializers import UserSerializer

class ProjetBlocSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjetBloc
        fields = '__all__'

class ProjetSerializer(serializers.ModelSerializer):
    blocs = ProjetBlocSerializer(many=True, read_only=True)
    annonce = AnnonceSerializer(read_only=True)

    class Meta:
        model = Projet
        fields = '__all__'

class CotisationProjetSerializer(serializers.ModelSerializer):
    projet = ProjetSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = CotisationProjet
        fields = '__all__'
        read_only_fields = ['montant_calcule', 'date_paiement'] 