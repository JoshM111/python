from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('dogs/new', views.new),
    path('dogs/create', views.create),
    path('dogs/<int:dogs_id>', views.show),
    path('dogs/<int:id>/destroy', views.delete),
    path('dogs/<int:id>/edit', views.edit),
]