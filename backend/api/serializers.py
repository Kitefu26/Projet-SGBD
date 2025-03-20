# filepath: /c:/Users/KHQRITOU FA/Desktop/Projet-SGBD/backend/api/serializers.py
from rest_framework import serializers
from exercices.models import Soumission, Correction

class SoumissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soumission
        fields = '__all__'

class CorrectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correction
        fields = '__all__'