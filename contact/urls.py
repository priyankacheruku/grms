from django.conf.urls import url
from django.urls import path
from . import views
from django.shortcuts import render
urlpatterns = [
    path('sendMail', views.sendMail, name='sendMail'),
    path('successmail',views.successmail,name='successmail'),
]
