import imp
from django.urls import path

from tailwindapp import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('<slug:slug>', views.getPosts, name='getPosts'),
    path('<slug:slug>', views.getProjects, name='getProjects')
]