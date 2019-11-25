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
#items added to cart
bill=[]
final=[]
#all items retived
items = item.objects.all()

#only item name are added
for i in items:
   	l.append(i.name)
total_amount=0

# Create your views here.
def index(request):
	bill.clear()
	final.clear()
	
	global total_amount
	return render(request, 'home.html', {'products':l,'total': "total_amount"})
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


@csrf_exempt
def update(request):
	print("ok......")
	if request.method == 'POST':

		itemid=int(request.POST['itemid'])
		print(itemid)
		e = item.objects.get(id_no=itemid)
		quantity=int(request.POST['quantity'])
		#print(e.name)
		user=request.user
		#print(user)
		try:

			cartItem=cartItems.objects.get(item_name=e,user=user)
			cartItem.quantity=quantity
			cartItem.save()
			#cart=cart.objects.get(user=user)
			#i=cartItems.objects.select_related('item_name')
			print(i)
			with connection.cursor() as cursor:
				cursor.execute("select sum(i.price*quantity)  from products_cartitems,products_item as i where user_id=1 and item_name_id=i.id")
				row = cursor.fetchone()
				print(row)
				#global context
				context =  {"row":row}
				return render(request, "cart.html", context)
			#my_custom_sql()
		except cartItems.DoesNotExist:
			cartItem=cartItems.objects.create(item_name=e,quantity=quantity,user=user)
			cartItem.save()
		#print(cartItem.objects.raw(select sum(i.price*quantity)  from cartitems,item as i where user=1 AND i.name=item_name))
		print(cartItems.objects.filter(user=1))
	
	
		