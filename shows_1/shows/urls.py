from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('shows/new/', views.new),
    path('/shows', views.shows),
    path('create/', views.create),
    path('shows/<int:id>', views.show),
    path('shows/<int:id>/edit', views.edit),
    path('shows/<int:id>/delete', views.delete),
    path('shows/<int:show_id>/update', views.update),
]