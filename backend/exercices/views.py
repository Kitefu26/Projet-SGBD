import requests
import sqlparse
import logging
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Avg
from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.routers import DefaultRouter

from .models import Exercice, Soumission, Correction, Sujet, SujetExamen, ModeleCorrection, Plagiat
from .serializers import (
    ExerciceSerializer, SoumissionSerializer, CorrectionSerializer,
    SujetSerializer, SujetExamenSerializer, ModeleCorrectionSerializer, PlagiatSerializer
)
from .plagiat import detect_plagiarism # Importer la fonction détecter le plagiat

# Configuration du logger
logger = logging.getLogger(__name__)

class ExerciceViewSet(viewsets.ModelViewSet):
    queryset = Exercice.objects.all()
    serializer_class = ExerciceSerializer

class SoumissionViewSet(viewsets.ModelViewSet):
    queryset = Soumission.objects.all().select_related('etudiant')
    serializer_class = SoumissionSerializer

    def perform_create(self, serializer):
        soumission = serializer.save()
        self.detect_plagiarism_in_soumission(soumission)

    def detect_plagiarism_in_soumission(self, soumission):
        """Appelle la détection du plagiat et enregistre les résultats."""
        text1 = soumission.exercice.description  # Texte de l'exercice
        text2 = soumission.fichier_soumission.read().decode('utf-8')  # Contenu soumis

        similarity_score = detect_plagiarism(text1, text2)

        # Enregistrer ou mettre à jour l'enregistrement de plagiat
        plagiat_instance, created = Plagiat.objects.get_or_create(soumission=soumission)
        plagiat_instance.score_plagiat = similarity_score
        plagiat_instance.details = f"Plagiat détecté avec un score de similarité de {similarity_score:.2f}"
        plagiat_instance.save()

        logger.info(f"Plagiat détecté pour la soumission {soumission.id}, score : {similarity_score}")

class CorrectionViewSet(viewsets.ModelViewSet):
    queryset = Correction.objects.all().select_related('soumission')
    serializer_class = CorrectionSerializer

class SujetViewSet(viewsets.ModelViewSet):
    queryset = Sujet.objects.all()
    serializer_class = SujetSerializer

class SujetExamenViewSet(viewsets.ModelViewSet):
    queryset = SujetExamen.objects.all()
    serializer_class = SujetExamenSerializer

class ModeleCorrectionViewSet(viewsets.ModelViewSet):
    queryset = ModeleCorrection.objects.all()
    serializer_class = ModeleCorrectionSerializer

class PlagiatViewSet(viewsets.ViewSet):
    queryset = Plagiat.objects.none()  # Utiliser un queryset vide pour éviter l'erreur

    @action(detail=False, methods=['post'])
    def detect(self, request):
        text1 = request.data.get('text1')
        text2 = request.data.get('text2')
        
        if not text1 or not text2:
            return Response({"error": "Both texts are required."}, status=400)

        # Appel de la fonction de détection de plagiat
        similarity_score = detect_plagiarism(text1, text2)
        
        # Optionnel : Créer un objet Plagiat dans la base de données
        soumission = Soumission.objects.first()  # Utilisez une logique pour trouver la soumission associée
        plagiat = Plagiat.objects.create(
            soumission=soumission,
            score_plagiat=similarity_score,
            details="Plagiat détecté entre les deux textes"
        )
        
        # Sérialiser l'objet Plagiat et retourner la réponse
        plagiat_serializer = PlagiatSerializer(plagiat)
        
        return Response({"similarity_score": similarity_score, "plagiat_details": plagiat_serializer.data})
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def corriger_reponse(request):
    """
    Corrige une soumission avec l'IA via Ollama.
    Expects JSON: {"soumission_id": <id>}
    """
    soumission_id = request.data.get('soumission_id')
    
    if not soumission_id:
        logger.warning("ID de soumission manquant dans la requête.")
        return Response({'error': "L'ID de soumission est requis."}, status=400)

    try:
        soumission = Soumission.objects.select_related('etudiant').get(id=soumission_id)
    except ObjectDoesNotExist:
        logger.error(f"Soumission introuvable pour l'ID {soumission_id}")
        return Response({'error': "Soumission introuvable."}, status=404)

    if not soumission.reponse:
        return Response({'error': "La réponse de la soumission est vide."}, status=400)

    try:
        api_response = requests.post(
            'http://localhost:11434/correct',
            json={'reponse': soumission.reponse},
            timeout=5
        )
        api_response.raise_for_status()
        data = api_response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Erreur lors de l'appel API de correction : {e}")
        return Response({'error': "Erreur de communication avec le service de correction."}, status=500)

    correction = Correction.objects.create(
        soumission=soumission,
        note=data.get('note', 0),
        feedback=data.get('feedback', "Pas de feedback fourni.")
    )

    return Response(CorrectionSerializer(correction).data)

@api_view(['POST'])
def analyser_syntaxe_sql(request):
    """
    Analyse la syntaxe d'une requête SQL avec sqlparse.
    Expects JSON: {"requete_sql": "<votre requête SQL>"}
    """
    requete_sql = request.data.get('requete_sql')
    
    if not requete_sql:
        return Response({"error": "La requête SQL est vide."}, status=400)

    try:
        parsed = sqlparse.parse(requete_sql)
        if not parsed:
            return Response({"error": "Requête SQL invalide."}, status=400)
        return Response({"message": "Requête SQL valide."})
    except Exception as e:
        logger.error(f"Erreur d'analyse SQL : {e}")
        return Response({"error": str(e)}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_performance(request):
    """
    Retourne la performance d'un étudiant.
    """
    student_id = request.user.id
    soumissions = Soumission.objects.filter(etudiant_id=student_id).only('date_soumission', 'note')

    if not soumissions.exists():
        return Response({'message': "Aucune soumission trouvée."}, status=404)

    performance = [{'date': s.date_soumission, 'note': s.note} for s in soumissions]
    class_average = soumissions.aggregate(avg_note=Avg('note'))['avg_note'] or 0

    return Response({
        'performance': performance,
        'class_average': round(class_average, 2)
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def professor_statistics(request):
    """
    Retourne les statistiques générales pour un professeur.
    """
    total_soumissions = Soumission.objects.count()

    if total_soumissions == 0:
        return Response({
            'total_soumissions': 0,
            'taux_reussite': 0,
            'questions_mal_comprises': [],
            'tendances_apprentissage': []
        })

    taux_reussite = (Soumission.objects.filter(note__gte=10).count() / total_soumissions) * 100

    questions_mal_comprises = list(
        Soumission.objects.values('question')
        .annotate(count=Count('question'))
        .order_by('-count')
    )[:5]

    tendances_apprentissage = ["Tendance 1", "Tendance 2", "Tendance 3"]

    return Response({
        'total_soumissions': total_soumissions,
        'taux_reussite': round(taux_reussite, 2),
        'questions_mal_comprises': questions_mal_comprises,
        'tendances_apprentissage': tendances_apprentissage
    })
