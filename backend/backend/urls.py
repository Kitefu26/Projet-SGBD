from django.contrib import admin
from django.urls import path, include
from api.views import home, upload_sujet, statistiques  # Vérifier si ces vues existent
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Routes principales
    path('', home, name='home'),
    path('upload_sujet/', upload_sujet, name='upload_sujet'),
    path('statistiques/', statistiques, name='statistiques'),

    # Authentification avec Django Allauth
    path('accounts/', include('allauth.urls')),

    # API (Vérifie que `exercices.urls` existe bien)
    path('api/', include('exercices.urls')),
]

# Servir les fichiers médias en mode développement uniquement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
