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
            print(hash_1)
            user = User.objects.create(
                name=request.POST['user_name'],
                email=request.POST['email'],
                password=hash_1
            )
            request.session['user_id'] = user.id
            return redirect('/main_page')#the main page of the application
    return redirect('/')
def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if len(user) > 0:
        user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user_id'] = user.id
            return redirect('/main_page')
    messages.error(request, "Stop it! Get some help!")
    return redirect('/')
def main_page(request):
    if 'user_id' not in request.session:
        messages.error(request, "Why you try to get around this?! Stop it and register or login!")
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'main_page.html', context)
    
def logout(request):
    request.session.clear()
    return redirect('/')