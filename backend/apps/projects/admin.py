from django.contrib import admin
from .models import Projet, ProjetBloc, CotisationProjet

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('nom', 'annonce', 'cout_total', 'date_debut', 'date_fin', 'statut')
    list_filter = ('statut', 'date_debut')
    search_fields = ('nom', 'description')
    ordering = ('-date_debut',)

@admin.register(ProjetBloc)
class ProjetBlocAdmin(admin.ModelAdmin):
    list_display = ('projet', 'bloc', 'est_inclus')
    list_filter = ('est_inclus', 'bloc')
    search_fields = ('projet__nom', 'bloc')

@admin.register(CotisationProjet)
class CotisationProjetAdmin(admin.ModelAdmin):
    list_display = ('projet', 'user', 'montant_calcule', 'est_paye', 'statut')
    list_filter = ('est_paye', 'statut')
    search_fields = ('projet__nom', 'user__username')
    ordering = ('-projet__date_debut',) 