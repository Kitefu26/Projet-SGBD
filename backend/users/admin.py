from django.contrib import admin
from .models import User

# Vérifiez si le modèle User est déjà enregistré
if not admin.site.is_registered(User):
    @admin.register(User)
    class UserAdmin(admin.ModelAdmin):
        list_display = ('username', 'first_name', 'last_name', 'email', 'role', 'date_inscription')