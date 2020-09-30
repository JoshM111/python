from django.shortcuts import render, HttpResponse, redirect
from dojo_ninjas_app.models import Dojo, Ninja 

def index(request):
    context = {
        'dojos': Dojo.objects.all()
    }
    return render(request, 'index.html', context)
def create_d(request):
    Dojo.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state'],
    )
    return redirect('/')
def create_n(request):
    Ninja.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        Dojo_id=request.POST['dojo'],
    )
    return redirect('/')