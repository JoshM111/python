from django.shortcuts import render, redirect
from .models import User, UserManager
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')
def register(request):
    if request.method == "POST":
        errors= User.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            hash_1= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            User.objects.create(
                name=request.POST['user_name'],
                email=request.POST['email'],
                password=hash_1
            )
            return redirect('main_page')#the main page of the application
    return redirect('/')