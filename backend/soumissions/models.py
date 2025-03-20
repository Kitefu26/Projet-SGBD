from django.db import models
from django.conf import settings
from cryptography.fernet import Fernet
from django.utils import timezone
class Exercice(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    fichier = models.FileField(upload_to='exercices/')
    date_depot = models.DateTimeField(auto_now_add=True)
    professeur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='exercices')

    def __str__(self):
        return self.titre

class Soumission(models.Model):
    exercice = models.ForeignKey(Exercice, on_delete=models.CASCADE, related_name='soumissions')
    etudiant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='soumissions')
    fichier_soumission = models.FileField(upload_to='soumissions/')
    fichier_chiffre = models.BinaryField(editable=False, null=True, blank=True)
    date_soumission = models.DateTimeField(auto_now_add=True)
    note = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    commentaire = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if self.fichier_soumission:
            key = Fernet.generate_key()
            cipher_suite = Fernet(key)
            with self.fichier_soumission.open('rb') as f:
                file_data = f.read()
            encrypted_data = cipher_suite.encrypt(file_data)
            self.fichier_chiffre = encrypted_data
        super(Soumission, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.etudiant.username} - {self.exercice.titre}"

class Correction(models.Model):
    soumission = models.ForeignKey(Soumission, on_delete=models.CASCADE, related_name='corrections')
    correcteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='corrections')
    note = models.DecimalField(max_digits=5, decimal_places=2)
    feedback = models.TextField(blank=True)
    date_correction = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=[('validé', 'Validé'), ('à réviser', 'À réviser')])

    def __str__(self):
        return f"Correction de {self.soumission.etudiant.username} pour {self.soumission.exercice.titre}"

class Sujet(models.Model):
    titre = models.CharField(max_length=200)
    fichier = models.FileField(upload_to='sujets/')

    def __str__(self):
        return self.titre

class SujetExamen(models.Model):
    titre = models.CharField(max_length=200)
    fichier = models.FileField(upload_to='sujets_examen/')

    def __str__(self):
        return self.titre

class ModeleCorrection(models.Model):
    exercice = models.ForeignKey(Exercice, on_delete=models.CASCADE, related_name='modeles_correction')
    correcteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='modeles_correcteur_corrections')
    fichier_correction = models.FileField(upload_to='modeles_correction/')
    date_modification = models.DateTimeField(auto_now=True)
    commentaires = models.TextField(blank=True)

    def __str__(self):
        return f"Modèle de correction pour {self.exercice.titre}"

class Plagiat(models.Model):
    soumission = models.ForeignKey(Soumission, on_delete=models.CASCADE, related_name='plagiats')
    score_plagiat = models.DecimalField(max_digits=5, decimal_places=2)
    details = models.TextField(blank=True)

    def __str__(self):
        return f"Plagiat pour {self.soumission.etudiant.username} - Score: {self.score_plagiat}"