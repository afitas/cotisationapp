from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import CustomUser, ConfigurationCite

class CustomUserTests(TestCase):
    def setUp(self):
        self.config = ConfigurationCite.objects.create(nombre_blocs=5)
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

    def test_user_creation(self):
        self.assertEqual(CustomUser.objects.count(), 2)
        self.assertTrue(self.admin.is_active)
        self.assertEqual(self.abonne.bloc, '1')

    def test_user_str(self):
        self.assertEqual(str(self.abonne), f"{self.abonne.get_full_name()} (1)")

class UserAPITests(APITestCase):
    def setUp(self):
        self.config = ConfigurationCite.objects.create(nombre_blocs=5)
        self.admin = CustomUser.objects.create_superuser(
            username='admin',
            password='admin123',
            email='admin@test.com'
        )
        self.client.force_authenticate(user=self.admin)

    def test_user_list(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_create(self):
        url = reverse('user-list')
        data = {
            'username': 'testuser',
            'password': 'test123',
            'role': 'abonne',
            'bloc': '1'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 2) 