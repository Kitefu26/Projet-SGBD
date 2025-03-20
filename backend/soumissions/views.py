from rest_framework import generics
from .models import Soumission
from .serializers import SoumissionSerializer

class SoumissionListCreateView(generics.ListCreateAPIView):
    queryset = Soumission.objects.all()
    serializer_class = SoumissionSerializer

class SoumissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Soumission.objects.all()
    serializer_class = SoumissionSerializer