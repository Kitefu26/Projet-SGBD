from rest_framework import serializers
from .models import User  # Ton modèle d'utilisateur personnalisé

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']  # Ajoute les champs que tu veux exposer
