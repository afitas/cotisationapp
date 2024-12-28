from django.db import models
from django.conf import settings
from apps.announcements.models import Annonce

class Projet(models.Model):
    STATUT_CHOICES = (
        ('en_attente', 'En Attente'),
        ('en_cours', 'En Cours'),
        ('termine', 'Terminé'),
        ('annule', 'Annulé'),
    )

    annonce = models.ForeignKey(
        'announcements.Annonce',
        on_delete=models.CASCADE,
        related_name='projets'
    )
    nom = models.CharField(max_length=200)
    description = models.TextField()
    cout_total = models.DecimalField(max_digits=10, decimal_places=2)
    date_debut = models.DateField()
    date_fin = models.DateField()
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='en_attente'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Projet'
        verbose_name_plural = 'Projets'

    def __str__(self):
        return self.nom

class ProjetBloc(models.Model):
    projet = models.ForeignKey(
        Projet,
        on_delete=models.CASCADE,
        related_name='blocs'
    )
    bloc = models.CharField(max_length=10)
    est_inclus = models.BooleanField(default=True)

    class Meta:
        unique_together = ('projet', 'bloc')

class CotisationProjet(models.Model):
    STATUT_CHOICES = (
        ('en_attente', 'En Attente'),
        ('paye', 'Payé'),
        ('en_retard', 'En Retard'),
    )

    projet = models.ForeignKey(
        Projet,
        on_delete=models.CASCADE,
        related_name='cotisations_projet'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cotisations_projet'
    )
    montant_calcule = models.DecimalField(max_digits=10, decimal_places=2)
    est_paye = models.BooleanField(default=False)
    date_paiement = models.DateTimeField(null=True, blank=True)
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='en_attente'
    )

    class Meta:
        verbose_name = 'Cotisation Projet'
        verbose_name_plural = 'Cotisations Projets' 