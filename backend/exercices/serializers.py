from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Exercice, Soumission, Correction, SujetExamen, ModeleCorrection, Sujet
from .plagiat import detect_plagiarism
from .models import Plagiat

# Sérialiseurs pour les modèles
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

class SujetExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = SujetExamen
        fields = '__all__'

class ModeleCorrectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeleCorrection
        fields = '__all__'

class SujetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sujet
        fields = '__all__'

# Vue pour détecter le plagiat
class PlagiatViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def detect(self, request):
        text1 = request.data.get('text1')
        text2 = request.data.get('text2')
        
        if not text1 or not text2:
            return Response({"error": "Both texts are required."}, status=400)

        # Appel de la fonction de détection de plagiat
        similarity_score = detect_plagiarism(text1, text2)
        
        return Response({"similarity_score": similarity_score})
class PlagiatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plagiat
        fields = ['id', 'soumission', 'score_plagiat', 'details']