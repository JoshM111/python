from django.shortcuts import render, redirect
from .models import Show
def index(request):
    return redirect('/shows')
def shows(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'index.html', context)
def new(request):
    return render(request, 'create.html')
def create(request):
    if request.method == "POST":
        Show.objects.create(
            title= request.POST['title'],
            network= request.POST['network'],
            release= request.POST['release'],
            desc= request.POST['desc'],
        )
    return redirect('/shows')
def edit(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    return render(request, 'edit.html',context)
def show(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    return render(request, 'show.html', context)
def update(request, show_id):
    to_update = Show.objects.get(id=show_id)
    to_update.titles = request.POST['title']
    to_update.release_date = request.POST['release']
    to_update.network = request.POST['network']
    to_update.description = request.POST['desc']
    to_update.save()
    return redirect('/shows')
def delete(request, show_id):
    to_delete = Show.objects.get(id=show_id)
    to_delete.delete()
    return redirect('/shows')