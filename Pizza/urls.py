from django import views
from django.urls import path
from . import views
from .models import Product
#aqui debo de gestionar las rutas de las paguinas web que quiero mostrar
urlpatterns = [
    path('home', views.home,name='home'),
    path('menu', views.menu,name='menu'),
    path('contact', views.contact,name='contact'),
    path('my_ordens', views.my_ordens,name='my_ordens'),

    #requerimos el id de la pizza que se está procesando
    path('add_pizza_to_orden/<int:id_product>',views.add_product_to_orden ,name='add_pizza_to_orden'),

    path('currently_orden',views.currently_orden,name='currently_orden'),
    #ruta para agregar un item al carrito de compras
    path('add_item_to_car/<int:id_product>',views.add_item_to_car,name='add_item_to_car')
]