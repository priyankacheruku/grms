from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
class item(models.Model):
    name = models.CharField(max_length=255)
    id_no= models.IntegerField()
    content = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    price= models.IntegerField()
   