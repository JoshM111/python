from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('ninja/create', views.create_n),
    path('dojo/create', views.create_d),
]