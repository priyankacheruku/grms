from django.shortcuts import render
from django.http import HttpResponse
from django.db import models

from products.models import *
# Create your views here.

items = item.objects.all()
l=[]
for i in items:
	l.append(i.name)
def home(request):
	context = {"home_page": "active"}
	return render(request, 'home.html',context)
def search(request):
	context = {
		"search_page": "active",
		'products':l,
	}
	return render(request, 'search.html',context)
def cart(request):
	
	context={
		"cart_page": "active",
		'items':items,
	}
	return render(request, 'cart.html',context)
def contact(request):
	context = {"contact_page": "active"}
	return render(request, 'contact.html',context)