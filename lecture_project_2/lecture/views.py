from django.shortcuts import render, redirect
from .models import User, Koala
from django.contrib import messages
import bcrypt
from django.db.models import Count
def index(request):
    return render(request, 'index.html')
def register(request):
    if request.method == "POST":
        errors= User.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            hash_1= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            print(hash_1)
            user = User.objects.create(
                name=request.POST['user_name'],
                email=request.POST['email'],
                password=hash_1
            )
            request.session['user_id'] = user.id
            return redirect('/main_page')#the main page of the application
    return redirect('/')
def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if len(user) > 0:
        user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user_id'] = user.id
            return redirect('/main_page')
    messages.error(request, "Stop it! Get some help!")
    return redirect('/')
def main_page(request):
    if 'user_id' not in request.session:
        messages.error(request, "Why you try to get around this?! Stop it and register or login!")
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'all_koalas': Koala.objects.all(),
    }
    return render(request, 'main_page.html', context)
    
def logout(request):
    request.session.clear()
    return redirect('/')
def create_koala(request):
    if request.method == "POST":
        errors = Koala.objects.create_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request,value)
        # return redirect('/main_page')
        else:
            koala = Koala.objects.create(name=request.POST['koala_name'], talent=request.POST['talent'], user=User.objects.get(id=request.session['user_id']))
            # return redirect('/main_page')
    return redirect('/main_page')
def user(request):
    if 'user_id' not in request.session:
        messages.error(request, "Why you try to get around this?! Stop it and register or login!")
        return redirect('/')
    context = {
        "user": User.objects.get(id=request.session['user_id']),
    }
    return redirect(request, "profile.html", context)
def show(request, id):
    if 'user_id' not in request.session:
        messages.error(request, "Why you try to get around this?! Stop it and register or login!")
        return redirect('/')
    koala_with_id = Koala.objects.filter(id=id)
    if len(koala_with_id) > 0:
        context = {
            "koala": Koala.objects.get(id=id)
        }
        return render(request, "koala.html", contect)
    else:
        return redirect('/user')
def delete_koala(request, id):
    if 'user_id' not in request.session:
        messages.error(request, "Why you try to get around this?! Stop it and register or login!")
        return redirect('/')
    if request.method == "POST":
        koala_with_id = Koala.objects.filter(id=id)
    if len(koala_with_id) > 0:
        koala = Koala.objects.get(id=id)
    if koala.user.id  == request.session['user_id']:
        koala.delete()
    return redirect('/main_page')
def voting_page(request):
    if 'user_id' not in request.session:
        messages.error(request, "Why you try to get around this?! Stop it and register or login!")
        return redirect('/')
    context= {
        "all_koalas": Koala.objects.annotate(votes=Count('users_vote')).order_by('-votes'),
        "user": User.objects.get(id=request.session['user_id']),
    }
    return render(request, "voting_page.html", context)
def vote_koala(request, id):
    if request.method == "POST":
        koala_with_id =  Koala.objects.filter(id=id)
        if len(koala_with_id) > 0:
            koala = Koala.objects.get(id=id)
            user = User.objects.get(id=request.session['user_id'])
            koala.users_vote.add(user)
            # user.voted_koalas.add(koala) doesnt matter which one that you use
        return redirect('/voting')
def unvote_koala(request, id):
    if request.method == "POST":
        koala_with_id =  Koala.objects.filter(id=id)
        if len(koala_with_id) > 0:
            koala = Koala.objects.get(id=id)
            user = User.objects.get(id=request.session['user_id'])
            koala.users_vote.remove(user)
            # user.voted_koalas.add(koala) doesnt matter which one that you use
        return redirect('/voting')