from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import Exercice, Soumission, Correction, SujetExamen, ModeleCorrection
from api.forms import SoumissionForm
from .serializers import ExerciceSerializer, SoumissionSerializer, CorrectionSerializer, SujetExamenSerializer, ModeleCorrectionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic import ListView, CreateView

class ExerciceViewSet(viewsets.ModelViewSet):
    queryset = Exercice.objects.all()
    serializer_class = ExerciceSerializer

class SujetExamenViewSet(viewsets.ModelViewSet):
    queryset = SujetExamen.objects.all()
    serializer_class = SujetExamenSerializer

class ModeleCorrectionViewSet(viewsets.ModelViewSet):
    queryset = ModeleCorrection.objects.all()
    serializer_class = ModeleCorrectionSerializer

class SoumissionViewSet(viewsets.ModelViewSet):
    queryset = Soumission.objects.all()
    serializer_class = SoumissionSerializer

class ExerciceListCreateView(ListView, CreateView):
    model = Exercice
    template_name = 'exercice_list_create.html'
    fields = ['titre', 'description']

def submit_response(request):
    if request.method == 'POST':
        form = SoumissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SoumissionForm()
    return render(request, 'submit_response.html', {'form': form})