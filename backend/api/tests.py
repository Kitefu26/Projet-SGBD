import os
from django.test import TestCase

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

from rest_framework import status
from rest_framework.test import APIClient
from api.models import Soumission, Correction


class ApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.soumission = Soumission.objects.create(reponse="Test response")

    def test_corriger_reponse_success(self):
        response = self.client.post('/api/corriger/', {'soumission_id': self.soumission.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_corriger_reponse_invalid_id(self):
        response = self.client.post('/api/corriger/', {'soumission_id': 999})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_analyser_syntaxe_success(self):
        response = self.client.post('/api/analyser/', {'reponse': "Test response"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_analyser_syntaxe_invalid_data(self):
        response = self.client.post('/api/analyser/', {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_noter_reponse_success(self):
        response = self.client.post('/api/noter/', {'reponse': "Test response"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_noter_reponse_invalid_data(self):
        response = self.client.post('/api/noter/', {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_generer_feedback_success(self):
        response = self.client.post('/api/feedback/', {'reponse': "Test response"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_generer_feedback_invalid_data(self):
        response = self.client.post('/api/feedback/', {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
