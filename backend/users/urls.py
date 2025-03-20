from django.urls import path
from .views import get_users

urlpatterns = [
    path('api/users/', get_users),
]
