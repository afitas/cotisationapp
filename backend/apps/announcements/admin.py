from django.contrib import admin
from .models import Annonce

@admin.register(Annonce)
class AnnonceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'est_cotisable', 'date_creation', 'created_by', 'est_active')
    list_filter = ('est_cotisable', 'est_active', 'date_creation')
    search_fields = ('titre', 'contenu')
    ordering = ('-date_creation',) 