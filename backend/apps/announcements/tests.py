from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Annonce
from apps.users.models import CustomUser
from apps.projects.models import Projet

class AnnouncementModelsTests(TestCase):
    def setUp(self):
        self.admin = CustomUser.objects.create_user(
            username='admin',
            password='admin123',
            role='admin'
        )
        self.annonce = Annonce.objects.create(
            titre="Test Annonce",
            contenu="Description de test",
            est_cotisable=True,
            created_by=self.admin
        )

    def test_annonce_creation(self):
        self.assertEqual(Annonce.objects.count(), 1)
        self.assertEqual(str(self.annonce), "Test Annonce")
        self.assertTrue(self.annonce.est_active)

    def test_annonce_with_projet(self):
        projet = Projet.objects.create(
            annonce=self.annonce,
            nom="Projet lié",
            description="Description projet",
            cout_total=1000,
            date_debut=timezone.now().date(),
            date_fin=timezone.now().date()
        )
        self.assertEqual(self.annonce.projets.count(), 1)
        self.assertEqual(self.annonce.projets.first(), projet)

class AnnouncementAPITests(APITestCase):
    def setUp(self):
        self.admin = CustomUser.objects.create_superuser(
            username='admin',
            password='admin123'
        )
        self.client.force_authenticate(user=self.admin)

    def test_create_annonce(self):
        url = reverse('annonce-list')
        data = {
            'titre': "Nouvelle Annonce",
            'contenu': "Contenu de test",
            'est_cotisable': True
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Annonce.objects.count(), 1)

    def test_list_annonces(self):
        Annonce.objects.create(
            titre="Test 1",
            contenu="Contenu 1",
            created_by=self.admin
        )
        Annonce.objects.create(
            titre="Test 2",
            contenu="Contenu 2",
            created_by=self.admin
        )
        
        url = reverse('annonce-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_annonce(self):
        annonce = Annonce.objects.create(
            titre="Test",
            contenu="Contenu",
            created_by=self.admin
        )
        
        url = reverse('annonce-detail', kwargs={'pk': annonce.pk})
        data = {
            'titre': "Test Modifié",
            'contenu': "Contenu modifié"
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        annonce.refresh_from_db()
        self.assertEqual(annonce.titre, "Test Modifié") 