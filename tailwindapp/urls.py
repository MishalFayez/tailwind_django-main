import imp
from django.urls import path

from tailwindapp import views

urlpatterns = [
    path('', views.index, name='index')
]