from django.shortcuts import render, redirect
# from .models import Show

def index(request):
    return redirect('/shows')
def shows(request):
    # context = {
    #     'all_shows': Show.objects.all()
    # }
    return render(request, 'index.html')


def new(request):
    return render(request, 'create.html')
