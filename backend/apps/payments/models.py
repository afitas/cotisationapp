from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class Payment(models.Model):
    TYPE_CHOICES = (
        ('mensuel', 'Mensuel'),
        ('projet', 'Projet'),
    )

    cotisation = models.ForeignKey(
        'subscriptions.Cotisation',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='payments'
    )
    cotisation_projet = models.ForeignKey(
        'projects.CotisationProjet',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='payments'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField(blank=True)
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='payments_created'
    )

    def clean(self):
        if self.cotisation and self.cotisation_projet:
            raise ValidationError("Un paiement ne peut pas être associé à la fois à une cotisation mensuelle et à une cotisation projet")
        if not self.cotisation and not self.cotisation_projet:
            raise ValidationError("Un paiement doit être associé soit à une cotisation mensuelle soit à une cotisation projet") 