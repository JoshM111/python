from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
def random_word(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] = 0
    request.session['word'] += 1
    request.session['word'] = get_random_string(length=14)
    return render(request, 'rwg.html')
def reset(request):
    request.session.flush()
    return redirect('/random_word')

# Create your views here.
