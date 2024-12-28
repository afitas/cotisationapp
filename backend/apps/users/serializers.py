from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'first_name', 'last_name', 'bloc']
        read_only_fields = ['date_creation', 'derniere_modification']

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'role', 'telephone', 'address', 'bloc', 'nombre_voitures',
            'est_actif', 'date_creation', 'derniere_modification'
        ]
        read_only_fields = ['date_creation', 'derniere_modification'] 