from django.db import models
from django.conf import settings

class AnneeAbonnement(models.Model):
    annee = models.IntegerField(unique=True)
    est_actif = models.BooleanField(default=True)
    est_cloture = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_cloture = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='annees_abonnement_crees'
    )

    class Meta:
        verbose_name = 'Année d\'abonnement'
        verbose_name_plural = 'Années d\'abonnement'

    def __str__(self):
        return f"Année {self.annee}"

    def cloturer_annee(self):
        from django.utils import timezone
        self.est_cloture = True
        self.date_cloture = timezone.now()
        self.save()

class PlanMensuel(models.Model):
    annee = models.ForeignKey(
        AnneeAbonnement,
        on_delete=models.CASCADE,
        related_name='plans_mensuels'
    )
    mois = models.IntegerField(choices=[(i, i) for i in range(1, 13)])
    montant_conciergerie = models.DecimalField(max_digits=10, decimal_places=2)
    montant_par_voiture = models.DecimalField(max_digits=10, decimal_places=2)
    date_limite_paiement = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='plans_mensuels_crees'
    )

    class Meta:
        verbose_name = 'Plan mensuel'
        verbose_name_plural = 'Plans mensuels'
        unique_together = ('annee', 'mois')

    def __str__(self):
        return f"Plan {self.mois}/{self.annee.annee}"

    def calculer_montant(self, nombre_voitures):
        return self.montant_conciergerie + (self.montant_par_voiture * nombre_voitures)

class Cotisation(models.Model):
    STATUT_CHOICES = (
        ('en_attente', 'En Attente'),
        ('paye', 'Payé'),
        ('en_retard', 'En Retard'),
        ('annule', 'Annulé'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cotisations'
    )
    plan = models.ForeignKey(
        PlanMensuel,
        on_delete=models.CASCADE,
        related_name='cotisations'
    )
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='en_attente'
    )
    date_paiement = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cotisations_crees'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cotisation'
        verbose_name_plural = 'Cotisations' 