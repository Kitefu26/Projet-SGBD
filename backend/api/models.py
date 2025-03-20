from django.db import models

# Create your models here.


class Sujet(models.Model):
    titre = models.CharField(max_length=200)
    fichier = models.FileField(upload_to='sujets/')

    def __str__(self):
        return self.titre

class Exercice(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.titre

class Soumission(models.Model):
    etudiant = models.CharField(max_length=100)
    exercice = models.ForeignKey(Exercice, on_delete=models.CASCADE)
    date_soumission = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.etudiant} - {self.exercice}"

class Correction(models.Model):
    soumission = models.ForeignKey(Soumission, on_delete=models.CASCADE)
    correcteur = models.CharField(max_length=100)
    note = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.soumission} - {self.correcteur}"

class SujetExamen(models.Model):
    titre = models.CharField(max_length=200)
    fichier = models.FileField(upload_to='sujets/')

    def __str__(self):
        return self.titre

class ModeleCorrection(models.Model):
    sujet_examen = models.ForeignKey(SujetExamen, on_delete=models.CASCADE)
    correcteur = models.CharField(max_length=100)
    fichier = models.FileField(upload_to='modeles_correction/')

    def __str__(self):
        return f"{self.sujet_examen} - {self.correcteur}"