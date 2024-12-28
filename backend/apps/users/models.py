from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class ConfigurationCite(models.Model):
    nombre_blocs = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100)
        ],
        help_text="Nombre total de blocs dans la cité"
    )
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Configuration de la cité"
        verbose_name_plural = "Configuration de la cité"

    def __str__(self):
        return f"Configuration ({self.nombre_blocs} blocs)"

    @staticmethod
    def get_blocs_choices():
        config = ConfigurationCite.objects.first()
        if not config:
            config = ConfigurationCite.objects.create(nombre_blocs=1)
        return [(str(i), f'Bloc {i}') for i in range(1, config.nombre_blocs + 1)]

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrateur'),
        ('abonne', 'Abonné'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='abonne')
    telephone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    bloc = models.CharField(
        max_length=10,
        blank=True,
        choices=[],  # Sera rempli dynamiquement
        help_text="Numéro du bloc"
    )
    nombre_voitures = models.IntegerField(default=0)
    est_actif = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    derniere_modification = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'

    def __str__(self):
        return f"{self.get_full_name()} ({self.bloc})" 

    def clean(self):
        super().clean()
        if self.role == 'abonne' and not self.bloc:
            raise ValidationError("Le numéro de bloc est obligatoire pour les abonnés") 