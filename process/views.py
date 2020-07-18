from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):

    cities=Destination.objects.all()
    return render(request,"index.html",{"cities":cities})

def aboutus(request):
    return render(request,"aboutus.html")