from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExerciceViewSet, SoumissionViewSet, CorrectionViewSet

router = DefaultRouter()
router.register(r'exercices', ExerciceViewSet)
router.register(r'soumissions', SoumissionViewSet)
router.register(r'corrections', CorrectionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
