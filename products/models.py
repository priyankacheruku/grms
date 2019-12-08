from django.db import models
import datetime
# Create your models here.
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
class item(models.Model):
	def __str__(self):
		return 'item: '+self.name
	name = models.CharField(max_length=255)
	id_no= models.IntegerField(unique=True)
	content = models.TextField(blank=True)
	created_on = models.DateTimeField(auto_now_add=True)
	price= models.IntegerField()
	image = models.ImageField(upload_to='uploads/', verbose_name='image')
	class Meta:
   		ordering=['name']
class cartItems(models.Model):
	
	item_name=models.ForeignKey(item,on_delete=models.CASCADE,related_name="names")
	quantity=models.IntegerField()
	user = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE,related_name="users")
	def __str__(self):
		return('cart  items of '+self.user.username+' '+str(self.item_name))
	@property
	def lineTotal(self):
		return self.quantity *self.item_name.price
	

class cart(models.Model):
	def __str__(self):
		return 'cart of '+self.user.username+' on '+str(datetime.date.today())
	user = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE,related_name="+")
	created_on = models.DateTimeField(auto_now_add=True)
	totalPrice= models.IntegerField()
