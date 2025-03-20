# filepath: /c:/Users/KHQRITOU FA/Desktop/Projet-SGBD/backend/api/views.py
import requests
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from exercices.models import Soumission, Correction
from .serializers import SoumissionSerializer, CorrectionSerializer

@api_view(['POST'])
def corriger_reponse(request):
    soumission_id = request.data.get('soumission_id')
    soumission = Soumission.objects.get(id=soumission_id)
    reponse = soumission.reponse

    # Envoyer la réponse à l'API de DeepSeek via Ollama
    response = requests.post('https://api.deepseek.com/correct', json={'reponse': reponse})
    data = response.json()

    # Créer une correction basée sur la réponse de l'IA
    correction = Correction.objects.create(
        soumission=soumission,
        note=data['note'],
        feedback=data['feedback']
    )

    return Response(CorrectionSerializer(correction).data)

@api_view(['POST'])
def analyser_syntaxe(request):
    reponse = request.data.get('reponse')

    # Envoyer la réponse à l'API de DeepSeek via Ollama pour analyse syntaxique
    response = requests.post('https://api.deepseek.com/analyse', json={'reponse': reponse})
    data = response.json()

    return Response(data)

@api_view(['POST'])
def noter_reponse(request):
    reponse = request.data.get('reponse')

    # Envoyer la réponse à l'API de DeepSeek via Ollama pour notation
    response = requests.post('https://api.deepseek.com/note', json={'reponse': reponse})
    data = response.json()

    return Response(data)

@api_view(['POST'])
def generer_feedback(request):
    reponse = request.data.get('reponse')

    # Envoyer la réponse à l'API de DeepSeek via Ollama pour génération de feedback
    response = requests.post('https://api.deepseek.com/feedback', json={'reponse': reponse})
    data = response.json()

    return Response(data)

def home(request):
    return HttpResponse("Page d'accueil")

def upload_sujet(request):
    return HttpResponse("Upload du sujet")

def statistiques(request):
    return HttpResponse("Statistiques")