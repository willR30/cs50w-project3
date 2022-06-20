from itertools import product
from tabnanny import check
from unicodedata import category, name
from django.shortcuts import render,HttpResponseRedirect, redirect
from .models import Category, Orden, Product
from django.contrib.auth.models import User
from django.contrib.auth import logout
from Autentication.urls import *
# Create your views here.

#se agregan los items temporalmente
#una vez confirmada la orden se limpia la lista para volverse a usar
items_list_for_open_orden=[]
def home(request):
    #validamos el estado de la sesion
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return redirect("login")

def menu(request):
    products=get_menu_items()
    return render(request,'menu.html',products)


#solo muesra la vista con los detalles del producto
def add_product_to_orden(request,id_product):
    product_information=get_product_information_by_id(id_product)
    validate_is_last_orden_open(request)
    return render(request,'add_to_orden_car.html',product_information)

def contact(request):
    return render(request,'contact.html')


#vista para visualizar la orden actual
#el producto a factuar,los detalles de la orden, la cantidad
#el presio que se va a pagar por todo eso
def currently_orden(request):
    data={
        'OrdenItems':items_list_for_open_orden
    }
    return render(request,'currently_orden.html',data)

def get_current_user_id(request):
    current_user = request.user
    return current_user.id


def get_product_information_by_id(id):
    data={
        'product':Product.objects.filter(id_product=id)
    }
    
    return data

def get_category_products():
    category={
        'categorys': Category.objects.all()
    }
    return category
def get_menu_items():
    data = {
        'productos': Product.objects.all()
    }   
    return data
    

#Mostrar todos los items dentro de una orden
def open_orden_view():
    pass


def my_ordens(request):
    user_id=get_current_user_id(request)#pasamos el objeto request como parámetro
    data=get_order_by_user(user_id)
    return render(request,'my_ordens.html',data)

def get_order_by_user(id_user):
    data={
        'ordens':Orden.objects.filter(id_user=id_user)
    }
    return data


#primero debe de crearse una orden
def create_orden():
    pass

#se valida si la ultima orden creada ya fué cerrada
#si la ultima aun está en proceso, no se podrán agregar nuevas
#si la ultima orden está cerrada si se puede agregar una nueva
#Si el usuario no tiene ordenes se crea una 

def validate_is_last_orden_open(request):
    current_user=get_current_user_id(request)
    orden=Orden.objects.filter(id_user=current_user).last()
    print(orden.state)
    if orden.state =="Confirmed":
        print("La orden está confirmada")
    else:
        print("jajajaj")
    #Validamos si la orden está abierta

#se creara un objeto a partir de esta clase a fin de crear el item de la orden
class itemSaleObject:
    def __init__(self, product_item,amount,details,sub_total):
        self.product_item=product_item #se guarda el producto completo como objeto
        self.amount=amount #La cantidad de pizzas que va a compras
        self.details=details #La cantidad de ingredientes que lleva
        self.sub_total=sub_total #el precio del producto * la cantidad que esta comprando
    def __str__(self):
        return f'{self.product_item}-{self.amount}-{self.details}-{self.sub_total}'

def add_item_to_car(request,id_product):
    if request.method =='POST':
        #Obtenemos la info de ese producot
        this_product=get_product_information_by_id(id_product)
        #obtenemos el precio del producto
        product_price=this_product['product'][0].price
        product_amount=this_product['product'][0].amount_toppings
        
        #obtenemos la cantidad y los ingredientes
        amount_product=request.POST['txt_amount']
        check_list=request.POST['toppings_list'].split(',')

        print(f'==> ingredientes {len(check_list)}')
        print(f'Cantidad a comprar {amount_product}')
        #validamos si la cantidad de ingredientes agregados son los permitidos por el producto
        if len(check_list)>product_amount:
            print("Has sobrepasado el numero de ingredientes permitidos")
            #agregar mensaje
        else:
            print("todo bien XD")
            itemOrdenSale=itemSaleObject(this_product,amount_product,"Peperoni",(float(amount_product)*product_price))

            #agregamos el item a la lista que maneja los elementos de nuesta orden
            items_list_for_open_orden.append(itemOrdenSale)

            #Mostramos temporalmente la orden
            for pro in items_list_for_open_orden:
                print(f'Items de orden: {pro}')

            return redirect("menu")

#necesito saber que productos estan agregados en carrito de compras para que
#el usuario complete la orden 
#esta podrá cancelar la orden maximo 10 minutos despues de haberla hecho

#se va poder cancelar una orden
#mientras la orden no sea terminada y no se limpien los campos la orden estará en proceso
#una vez se cancela la orden se debe eliminar de la base de datos