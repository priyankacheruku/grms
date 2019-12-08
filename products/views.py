from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect,csrf_exempt
# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse

from django.db import models
from .models import *
from django.db import connection

#items in database will be added
l=[]

#all items retived
items = item.objects.all()

#only item name are added for search
for i in items:
   	l.append(i.name)


# Create your views here.
def index(request):
	return render(request, 'home.html')

def add(request):
	entry=[]
	x=request.GET["item_name"]
	
	try:
		entry = item.objects.get(name=x)
		#print(entry)
	except IndexError:
		return HttpResponse("null or unavailable value entered is  not accepted")
	except :
		return HttpResponse("null or unavailable value entered is  not accepted while search")

	context={
		'items':item,
		'products':l,
		
		'entry':entry
	}

	return render(request, 'search.html', context)


@csrf_exempt
def update(request):
	
	if request.method == 'POST':

		itemid=int(request.POST['itemid'])
		e = item.objects.get(id_no=itemid)
		quantity=int(request.POST['quantity'])
		user=request.user
		
		try:

			cartItem=cartItems.objects.get(item_name=e,user=user)
			cartItem.quantity=quantity
			cartItem.save()
			total=getTotal(request)
			context =  {"row":total}
				
		except cartItems.DoesNotExist:
		
			cartItem=cartItems.objects.create(item_name=e,quantity=quantity,user=user)
			cartItem.save()
			total=getTotal(request)
			context =  {"row":total}

		return JsonResponse(context)

def generate_invoice(request):
	items=item.objects.all()
	#print(items)
	cartitems=cartItems.objects.filter(user=request.user)
	total=getTotal(request)
	carts=cart.objects.create(user=request.user,totalPrice=total)
	context={
		'item':items,
		'cartItems':cartitems,
		'total':total
	}
	return render(request,'invoice.html',context)

@csrf_exempt
def delete(request):
	if request.method == 'POST':
		#print("ok")
		cartItems.objects.filter(user=request.user).delete()
		return JsonResponse({'success':"success"})

def getTotal(request):
	with connection.cursor() as cursor:
		id= int(request.user.id)
		cursor.execute("select sum(i.price*quantity)  from products_cartitems,products_item as i where user_id=%s and item_name_id=i.id",[int(id)])
		row = cursor.fetchone()
	return(row[0])