from django import forms
from exercices.models import Sujet, Soumission

class SujetForm(forms.ModelForm):
    class Meta:
        model = Sujet
        fields = ['titre', 'fichier']

class SoumissionForm(forms.ModelForm):
    class Meta:
        model = Soumission
        fields = ['exercice', 'etudiant', 'fichier', 'note', 'commentaire']