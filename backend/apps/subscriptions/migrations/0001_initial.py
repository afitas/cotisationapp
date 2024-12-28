# Generated by Django 5.0 on 2024-12-28 18:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnneeAbonnement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee', models.IntegerField(unique=True)),
                ('est_actif', models.BooleanField(default=True)),
                ('est_cloture', models.BooleanField(default=False)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_cloture', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annees_abonnement_crees', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': "Année d'abonnement",
                'verbose_name_plural': "Années d'abonnement",
            },
        ),
        migrations.CreateModel(
            name='PlanMensuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mois', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])),
                ('montant_conciergerie', models.DecimalField(decimal_places=2, max_digits=10)),
                ('montant_par_voiture', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_limite_paiement', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('annee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans_mensuels', to='subscriptions.anneeabonnement')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans_mensuels_crees', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Plan mensuel',
                'verbose_name_plural': 'Plans mensuels',
                'unique_together': {('annee', 'mois')},
            },
        ),
        migrations.CreateModel(
            name='Cotisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('statut', models.CharField(choices=[('en_attente', 'En Attente'), ('paye', 'Payé'), ('en_retard', 'En Retard'), ('annule', 'Annulé')], default='en_attente', max_length=20)),
                ('date_paiement', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cotisations_crees', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cotisations', to=settings.AUTH_USER_MODEL)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cotisations', to='subscriptions.planmensuel')),
            ],
            options={
                'verbose_name': 'Cotisation',
                'verbose_name_plural': 'Cotisations',
            },
        ),
    ]