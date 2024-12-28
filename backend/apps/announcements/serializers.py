from rest_framework import serializers
from .models import Annonce
from apps.users.serializers import UserSerializer

class AnnonceSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Annonce
        fields = '__all__'
        read_only_fields = ['created_by', 'date_creation'] 