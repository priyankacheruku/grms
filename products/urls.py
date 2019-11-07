from django.urls import path
from products import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    #path('add/',views.add, name='add')
    url(r'^add/$', views.add,name='add'),
    #url(r'^$', 'views.index'),
]
