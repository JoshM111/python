from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard),
    path('user/<int:id>', views.user_page),
    path('firstTemplate', views.firstTemplate),
    path('submission', views.submission),
    path('thank_you', views.thank_you),
    # path('<url>', views.catch_all), #always put this "catch-all" last.
]