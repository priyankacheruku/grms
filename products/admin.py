from django.contrib import admin

# Register your models here.
from products.models import *
  
admin.site.register(item)
admin.site.register(cart)
admin.site.register(cartItems)