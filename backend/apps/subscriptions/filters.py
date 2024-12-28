from django_filters import rest_framework as filters
from .models import Cotisation, PlanMensuel

class CotisationFilter(filters.FilterSet):
    annee = filters.NumberFilter(field_name='plan__annee__annee')
    mois = filters.NumberFilter(field_name='plan__mois')
    statut = filters.CharFilter(field_name='statut')
    
    class Meta:
        model = Cotisation
        fields = ['annee', 'mois', 'statut']

class PlanMensuelFilter(filters.FilterSet):
    annee = filters.NumberFilter(field_name='annee__annee')
    
    class Meta:
        model = PlanMensuel
        fields = ['annee', 'mois'] 