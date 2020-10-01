from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('shows/', views.shows),
    path('shows/new/', views.new),
    # path('/<int:id>', views.read),
    # path('/<int:id>/edit', views.update),
    # path('/<int:id>/destroy', views.delete),
]