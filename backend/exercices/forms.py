from django import forms
from .models import Exercice

class ExerciceForm(forms.ModelForm):
    class Meta:
        model = Exercice
        fields = ['titre', 'professeur', 'date_debut', 'date_fin']