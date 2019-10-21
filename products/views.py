from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.db import models

from .models import *

def index(request):
    #return HttpResponse('Hello, welcome to the index page.')
    l=[]
    items = item.objects.all()
    for i in items:
    	l.append(i.name)
    return render(request, 'home.html', {'products':l})
