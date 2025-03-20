# filepath: /c:/Users/KHQRITOU FA/Desktop/Projet-SGBD/backend/api/urls.py
from django.urls import path
from .views import corriger_reponse, analyser_syntaxe, noter_reponse, generer_feedback

urlpatterns = [
    path('corriger/', corriger_reponse, name='corriger_reponse'),
    path('analyser/', analyser_syntaxe, name='analyser_syntaxe'),
    path('noter/', noter_reponse, name='noter_reponse'),
    path('feedback/', generer_feedback, name='generer_feedback'),
]