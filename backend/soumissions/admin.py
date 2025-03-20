from django.contrib import admin
from .models import Exercice, Soumission, Correction

@admin.register(Exercice)
class ExerciceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description', 'date_depot')  # Assurez-vous que ces champs existent

class SoumissionAdmin(admin.ModelAdmin):
    list_display = ('exercice', 'etudiant', 'note')
    list_filter = ('exercice', 'note')

class CorrectionAdmin(admin.ModelAdmin):
    list_display = ('soumission', 'correcteur', 'note')
    list_filter = ('soumission', 'correcteur')

admin.site.register(Soumission, SoumissionAdmin)
admin.site.register(Correction, CorrectionAdmin)