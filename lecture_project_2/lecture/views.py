from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')
def register(request):
    if request.method == "POST":
        errors= User.objects.create_validator(requset.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.erro(request, value)
            return redirect('/')
        else:
            pass
            #create an account for User
    return redirect('/')