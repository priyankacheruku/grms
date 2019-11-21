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
items = item.objects.all().order_by('name')

#only item name are added
for i in items:
   	l.append(i.name)
total_amount=0
def index(request):
	bill.clear()
	final.clear()
	
	global total_amount
	total_amount=0
	return render(request, 'home.html', {'products':l,'total': total_amount})
    
def add(request):
	entry=[]
	x=request.GET["item_name"]
	bill.append(x)

	#query to get price and id of items enterd
	entry = item.objects.filter(name=x).values_list('name','price','id')
	print(entry)
	try:
		
		global total_amount
		total_amount=total_amount+entry[0][1]

	except IndexError:
		return HttpResponse("null or unavailable value entered is  not accepted")
		
	for e in entry:		
		final.append("<tr>")
		for i in e:
			final.append("<td>")
			final.append(str(i))
			final.append("</td>")
		final.append("</tr>")
		

	f=''.join(final)
	context={
		'items':item,
		'products':l,
		'bill_items':bill,
		'bill':f,
		'table_header':"<tr><th>Name</th><th>Price</th><th>Id</th></tr>",
		'total': total_amount
	}

	return render(request, 'search.html', context)