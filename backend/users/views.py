from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def get_users(request):
    users = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
    ]
    return JsonResponse(users, safe=False)
