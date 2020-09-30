from django.shortcuts import render, redirect
from .models import path
def index(request):
    context = {
        'all_dogs': Dog.objects.all() 
    }
    return render(request, "index.html", context)

def new(request):
    
    return render(request, 'create.html')
def create(request):
    Show.objects.create(
        Name=request.POST['name'],
        age=request.POST['age'],
        # release=request.POST['release'],
    )
    return redirect('/')
def show_dog(request, id):
    context = {
        "one_dog": Dog.objects.get(id=id)
    }
def delete_dog(request, id):
    if request.method == "POST":
        dog_to_delete = Dog.objects.get(id=id)
        dot_to_delete = Dog.objects.