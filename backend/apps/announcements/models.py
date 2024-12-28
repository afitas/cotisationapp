from django.db import models
from django.conf import settings

class Annonce(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    est_cotisable = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='annonces_creees'
    )
    est_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Annonce'
        verbose_name_plural = 'Annonces'
        ordering = ['-date_creation']

    def __str__(self):
        return self.titre 