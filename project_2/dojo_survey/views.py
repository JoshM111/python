from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, "index.html")
def result(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['user_name'],
            'location': request.POST['location'],
            'language': request.POST['language'],
            'comment': request.POST['textbox'],
        }
        return render(request, 'result.html', context)
    return render(request, 'result.html')
def some_function(request):
    request.session['name'] = request.POST['name']
    request.session['counter'] = 100
# Create your views here.
