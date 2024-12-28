from django.contrib import admin
from .models import AnneeAbonnement, PlanMensuel, Cotisation

@admin.register(AnneeAbonnement)
class AnneeAbonnementAdmin(admin.ModelAdmin):
    list_display = ('annee', 'est_actif', 'est_cloture', 'date_creation', 'date_cloture')
    list_filter = ('est_actif', 'est_cloture')
    search_fields = ('annee',)
    ordering = ('-annee',)

@admin.register(PlanMensuel)
class PlanMensuelAdmin(admin.ModelAdmin):
    list_display = ('annee', 'mois', 'montant_conciergerie', 'montant_par_voiture', 'date_limite_paiement')
    list_filter = ('annee', 'mois')
    search_fields = ('annee__annee',)
    ordering = ('-annee__annee', 'mois')

@admin.register(Cotisation)
class CotisationAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'montant_total', 'statut', 'date_paiement')
    list_filter = ('statut', 'plan__annee', 'plan__mois')
    search_fields = ('user__username', 'user__email')
    ordering = ('-plan__annee__annee', '-plan__mois') 