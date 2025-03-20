from django.urls import path
from .views import SoumissionListCreateView, SoumissionDetailView

urlpatterns = [
    path('', SoumissionListCreateView.as_view(), name='soumission-list-create'),
    path('<int:pk>/', SoumissionDetailView.as_view(), name='soumission-detail'),
]