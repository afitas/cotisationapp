from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Projet, ProjetBloc, CotisationProjet
from apps.users.models import CustomUser
from apps.announcements.models import Annonce

class ProjectModelsTests(TestCase):
    def setUp(self):
        self.admin = CustomUser.objects.create_user(
            username='admin',
            password='admin123',
            role='admin'
        )
        self.annonce = Annonce.objects.create(
            titre="Test Projet",
            contenu="Description",
            est_cotisable=True,
            created_by=self.admin
        )
        self.projet = Projet.objects.create(
            annonce=self.annonce,
            nom="Projet Test",
            description="Description",
            cout_total=1000,
            date_debut=timezone.now().date(),
            date_fin=timezone.now().date()
        )

    def test_projet_creation(self):
        self.assertEqual(str(self.projet), "Projet Test")
        self.assertEqual(self.projet.statut, 'en_attente')

class ProjectAPITests(APITestCase):
    def setUp(self):
        self.admin = CustomUser.objects.create_superuser(
            username='admin',
            password='admin123'
        )
        self.client.force_authenticate(user=self.admin)
        self.annonce = Annonce.objects.create(
            titre="Test",
            contenu="Test",
            created_by=self.admin
        )

    def test_create_projet(self):
        url = reverse('projet-list')
        data = {
            'annonce': self.annonce.id,
            'nom': "Nouveau Projet",
            'description': "Description",
            'cout_total': 1000,
            'date_debut': timezone.now().date(),
            'date_fin': timezone.now().date()
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 