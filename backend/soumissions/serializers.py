from rest_framework import serializers
from .models import Soumission

class SoumissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soumission
        fields = '__all__'
