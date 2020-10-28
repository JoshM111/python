from django.urls import path
from . import views
urlpatterns= [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('main_page', views.main_page),
    path('logout', views.logout),
    path('koalas/create', views.create_koala),
    path('user', views.user),
    path('koalas/show/<int:id>', views.show),
    path('koalas/delete/<int:id>', views.delete_koala),
    path('voting', views.voting_page),
    path('koalas/cast_vote/<int:id>', views.vote_koala),
    path('koalas/uncast_vote/<int:id>', views.unvote_koala),
]