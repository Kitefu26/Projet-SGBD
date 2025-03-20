from django.contrib import admin
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES = (
        ('professeur', 'Professeur'),
        ('etudiant', 'Étudiant'),
    )
    date_naissance = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLES)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_role_display()})"