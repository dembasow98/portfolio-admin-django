# Add the home page of django

# Path: core\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]