from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'amount', 'date_created', 'created_by')
    list_filter = ('type', 'date_created')
    search_fields = ('remarks', 'created_by__username')
    ordering = ('-date_created',)

    def get_cotisation_info(self, obj):
        if obj.cotisation:
            return f"Mensuelle - {obj.cotisation}"
        elif obj.cotisation_projet:
            return f"Projet - {obj.cotisation_projet}"
        return "N/A"
    get_cotisation_info.short_description = "Cotisation" 