from django.shortcuts import render, HttpResponse, redirect
from .models import Dragon
def index(request):
    context = {
        "all_dragons": Dragon.objects.all()
    } 
    return render(request, "index.html", context)
    

# Create your views here.
