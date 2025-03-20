from django.db import models
from soumissions.models import Soumission


class Correction(models.Model):
    soumission = models.OneToOneField(Soumission, on_delete=models.CASCADE)
    note_finale = models.FloatField()
    feedback = models.TextField()  # Détail des erreurs et points à revoir
    date_correction = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Correction de {self.soumission.etudiant.username} - Note : {self.note_finale}"
