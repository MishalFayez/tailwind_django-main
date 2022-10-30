from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Info
# Create your views here.
def index(request):
    info = Info.objects.all()
    context = {'info': info}
    return render(request, 'tailwindapp/index.html', context)