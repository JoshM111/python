from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
    return HttpResponse("placeholder to later display list of blogs")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blogs")
def create(request):
    return redirect('/')
# redirect- designed to send you to another route within the application
def show(request, number):
    return HttpResponse("placeholder to display blog number " + str(number))
def edit(request, number):
    return HttpResponse("placeholder to edit blog " + str(number))
def destroy(request, number):
    return redirect('/')
def display(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)