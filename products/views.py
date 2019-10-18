from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    #return HttpResponse('Hello, welcome to the index page.')
    return render(request, 'home.html', {'products':'products will be viewed here'})
