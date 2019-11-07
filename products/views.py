from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.db import models

from .models import *

#items in database will be added
l=[]
#items added to cart
bill=[]
final=[]
#all items retived
items = item.objects.all()

#only item name are added
for i in items:
   	l.append(i.name)


def index(request):
	bill.clear()
	final.clear()
	

	return render(request, 'home.html', {'products':l})
    
def add(request):
	entry=[]
	x=request.GET["item_name"]
	bill.append(x)

	#query to get price and id of items enterd
	entry = list(item.objects.filter(name=x).values_list('name','price','id'))



	for e in entry:		
		final.append("<tr>")
		for i in e:
			final.append("<td>")
			final.append(str(i))
			final.append("</td>")
		final.append("</tr>")
	

	f=''.join(final)
	context={
		'products':l,
		'bill_items':bill,
		'bill':f
	}
	return render(request, 'home.html', context)