
from django.urls import path, include
from .views import m
urlpatterns = [
    path('p', m, name='ayoub'),
    
]
