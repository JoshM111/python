from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')
def register(request):
    errors= User.objects.create_validator()
