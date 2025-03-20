from rest_framework import serializers
from exercices.models import Exercice, Soumission, Correction

class ExerciceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercice
        fields = '__all__'

class SoumissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soumission
        fields = '__all__'

class CorrectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correction
        fields = '__all__'
