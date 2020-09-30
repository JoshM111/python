from django.shortcuts import render, HttpResponse, redirect
import random
from datetime import datetime

def index(request):
    if not 'gold' in request.session or "activities" not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request, "index.html")
def process_money(request):
    if request.method == "POST":
        print("the form has been submitted")
        print(request.POST)
        if request.POST['building'] == 'farm':
            num = random.randint(10,20)
            request.session['gold'] += num
            request.session['activities'].append("You earned "+ str(num) + "! Yay!")
        elif request.POST['building'] == 'cave':
            num = random.randint(5,10)
            request.session['gold'] += num
            request.session['activities'].append("You earned "+ str(num) + "! Yay!")
        elif request.POST['building'] == 'house':
            num = random.randint(2,5)
            request.session['gold'] += num
            request.session['activities'].append("You earned "+ str(num) + "! Yay!")
        elif request.POST['building'] == 'casino':
            num = random.randint(-50,50)
            request.session['gold'] += num
            if num > 0:
                request.session['activities'].append("You earned "+ str(num) + "! Yay!")
            elif num == 0:
                request.session['activities'].append("You earned nothing!")
            else:
                request.session['activities'].append("You lost "+ str(num) + "! HAHA!")
    return redirect('/')
def reset(request):
    request.session.clear()
    return redirect('/')