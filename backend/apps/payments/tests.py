from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Payment
from apps.users.models import CustomUser
from apps.subscriptions.models import AnneeAbonnement, PlanMensuel, Cotisation
from apps.projects.models import Projet, CotisationProjet
from apps.announcements.models import Annonce

class PaymentModelsTests(TestCase):
    def setUp(self):
        # Création des utilisateurs
        self.admin = CustomUser.objects.create_user(
            username='admin',
            password='admin123',
            role='admin'
        )
        self.abonne = CustomUser.objects.create_user(
            username='abonne',
            password='abonne123',
            role='abonne',
            bloc='1'
        )

        # Création d'une cotisation mensuelle
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
        self.cotisation = Cotisation.objects.create(
            user=self.abonne,
            plan=self.plan,
            montant_total=100,
            created_by=self.admin
        )

        # Création d'un paiement
        self.payment = Payment.objects.create(
            cotisation=self.cotisation,
            amount=100,
            type='mensuel',
            created_by=self.admin
        )

    def test_payment_creation(self):
        self.assertEqual(Payment.objects.count(), 1)
        self.assertEqual(self.payment.amount, 100)
        self.assertEqual(self.payment.type, 'mensuel')

    def test_payment_validation(self):
        # Test qu'un paiement ne peut pas être associé à deux types de cotisation
        with self.assertRaises(Exception):
            annonce = Annonce.objects.create(
                titre="Test",
                contenu="Test",
                created_by=self.admin
            )
            projet = Projet.objects.create(
                annonce=annonce,
                nom="Projet Test",
                cout_total=1000,
                date_debut=timezone.now().date(),
                date_fin=timezone.now().date()
            )
            cotisation_projet = CotisationProjet.objects.create(
                projet=projet,
                user=self.abonne,
                montant_calcule=500
            )
            Payment.objects.create(
                cotisation=self.cotisation,
                cotisation_projet=cotisation_projet,
                amount=100,
                type='mensuel',
                created_by=self.admin
            )

class PaymentAPITests(APITestCase):
    def setUp(self):
        self.admin = CustomUser.objects.create_superuser(
            username='admin',
            password='admin123'
        )
        self.client.force_authenticate(user=self.admin)

        # Création d'une cotisation
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
        self.cotisation = Cotisation.objects.create(
            user=self.admin,
            plan=self.plan,
            montant_total=100,
            created_by=self.admin
        )

    def test_create_payment(self):
        url = reverse('payment-list')
        data = {
            'cotisation': self.cotisation.id,
            'amount': 100,
            'type': 'mensuel',
            'remarks': 'Test payment'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payment.objects.count(), 1)

    def test_list_payments(self):
        url = reverse('payment-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK) 