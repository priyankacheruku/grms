from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.home, name='home'),
    #url(r'^$', index, name='index'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart, name='cart'),
    path('contact/', views.contact, name='contact'),
]
