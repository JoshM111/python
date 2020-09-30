from django.shortcuts import render, HttpResponse, redirect
from .models import User
def index(request):
    context = {
        "all_the_users": User.objects.all()
    }
    return render(request, "index.html", context)
def submit(request):
    if request.method == "POST":
        User.objects.create(
            first_name=request.POST['fname'],
            last_name=request.POST['lname'],
            email_address=request.POST['email'],
            age=request.POST['age']
        )
    return redirect('/')
def reset(request):
    request.session.clear()
    return redirect('/')
