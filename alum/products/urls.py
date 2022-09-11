from django.urls import path
from . import views

urlpatterns = [
    path('',views.products_home,name='products_home'),
    path('', views.order, name='order'),
    path('other',views.other,name='other'),
    path('window',views.window,name='window'),
    path('doors',views.doors,name='doors'),
    path('fire_door',views.fire_door,name='fire_door'),
    path('dym_door',views.dym_door,name='dym_door'),
    path('patio', views.patio, name='patio'),
    path('sl', views.sl, name='sl'),
    path('fasad', views.fasad, name='fasad'),
    path('ms', views.ms, name='ms'),
    path('windowsill', views.windowsill, name='windowsill'),
    path('otliv', views.otliv, name='otliv'),
    path('callback', views.order, name='callback'),
    ]
