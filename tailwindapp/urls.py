import imp
from django.urls import path

from tailwindapp import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('posts/<slug:slug>', views.getPosts, name='getPosts'),
    path('projects/<str:pk>', views.getProjects, name='getProjects')
]