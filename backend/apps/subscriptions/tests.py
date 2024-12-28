from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework import status
from .models import AnneeAbonnement, PlanMensuel, Cotisation
from apps.users.models import CustomUser

class SubscriptionModelsTests(TestCase):
    def setUp(self):
        self.admin = CustomUser.objects.create_user(
            username='admin',
            password='admin123',
            role='admin'
        )
        self.annee = AnneeAbonnement.objects.create(
            annee=2024,
            created_by=self.admin
        )
        self.plan = PlanMensuel.objects.create(
            annee=self.annee,
            mois=1,
            montant_conciergerie=100,
            montant_par_voiture=50,
            date_limite_paiement=timezone.now(),
            created_by=self.admin
        )

    def test_plan_mensuel_calcul(self):
        montant = self.plan.calculer_montant(nombre_voitures=2)
        self.assertEqual(montant, 200)  # 100 + (50 * 2)

    def test_annee_cloture(self):
        self.annee.cloturer_annee()
        self.assertTrue(self.annee.est_cloture)
        self.assertIsNotNone(self.annee.date_cloture)

class SubscriptionAPITests(APITestCase):
    def setUp(self):
        self.admin = CustomUser.objects.create_superuser(
            username='admin',
            password='admin123'
        )
        self.client.force_authenticate(user=self.admin)

    def test_create_annee(self):
        url = reverse('anneeabonnement-list')
        data = {'annee': 2024}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_plan(self):
        annee = AnneeAbonnement.objects.create(
            annee=2024,
            created_by=self.admin
        )
        url = reverse('planmensuel-list')
        data = {
            'annee': annee.id,
            'mois': 1,
            'montant_conciergerie': 100,
            'montant_par_voiture': 50,
            'date_limite_paiement': timezone.now().date()
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 