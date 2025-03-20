from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ExerciceViewSet, SoumissionViewSet, CorrectionViewSet,
    SujetViewSet, SujetExamenViewSet, ModeleCorrectionViewSet,
    corriger_reponse, analyser_syntaxe_sql, student_performance, professor_statistics
)
from .views import PlagiatViewSet

router = DefaultRouter()
router.register(r'exercices', ExerciceViewSet)
router.register(r'soumissions', SoumissionViewSet)
router.register(r'corrections', CorrectionViewSet)
router.register(r'sujets', SujetViewSet)
router.register(r'sujets-examens', SujetExamenViewSet)
router.register(r'modele-corrections', ModeleCorrectionViewSet)
router.register(r'plagiat', PlagiatViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('corriger_reponse/', corriger_reponse, name='corriger_reponse'),
    path('analyser_syntaxe_sql/', analyser_syntaxe_sql, name='analyser_syntaxe_sql'),
    path('student_performance/', student_performance, name='student_performance'),
    path('professor_statistics/', professor_statistics, name='professor_statistics'),
]
