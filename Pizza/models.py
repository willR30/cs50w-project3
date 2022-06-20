from statistics import mode
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User

# Create your models here.

#una orden puede tener 3 estados
#Delivered = entregada
#confirmada= ya se despachó y falta a que llegue el mensajero
#En proceso= el usuario aun sigue agregando cosas
class State(models.Model):
    id_state=models.AutoField(primary_key=True) 
    state=models.CharField(max_length=10)

    def __str__(self):
        return f'{self.state}'

#las categorias organizan las pizzas 
#Regular Pizza, Sicilian Pizza, subs, Pasta, etc....
class Category(models.Model):
    id_category=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    desciption=models.CharField(max_length=50)
    
    #personalizamos la forma en la que se muestra el objeto en el modelo
    def __str__(self):
        return f'{self.name}'

#modelo de las ordenes
#una orden puede ser hecha por un usuario, en una fecha determinada
#un usuario puede hacer varias ordenes
class Orden(models.Model):
    id_orden=models.AutoField(primary_key=True)
    id_user=models.ForeignKey(User,on_delete=models.CASCADE)#Una orden es hecha por un usuario
    orden_date=models.DateTimeField(auto_now=True)
    state=models.ForeignKey(State,on_delete=models.CASCADE)#cada orden puede tener un estado
    Total=models.IntegerField()

    def __str__(self):
        return f'{self.id_user} {self.orden_date} {self.state} {self.Total}'


#En este caso manejaremos 2 tipos de pizza small and large
class Type(models.Model):
    id_type=models.AutoField(primary_key=True)
    name=models.CharField(max_length=10)

    #al referenciarse con este objeto, retornaremos unicamente el nombre en lugar del id
    def __str__(self):
        return f'{self.name}'


#un producto puede pertenecer a una categoria y tener un precio diferente por cada tipo
#Pizza de Queso,Pizzas clásicas, pequeña, 200 cordobas
class Product(models.Model):
    id_product=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    id_category=models.ForeignKey(Category,on_delete=models.CASCADE)#Cada producto pertence a una categoria
    id_type=models.ForeignKey(Type,on_delete=models.CASCADE)#Cada producto tiene un tipo asociado
    amount_toppings=models.IntegerField(null=True, blank=True)
    price=models.FloatField()

    #Esta funcion indica  que y como mostrar en el admin este objeto
    def __str__(self): 
        return f'{self.id_product}-{self.name} - {self.id_category} - {self.id_type} - C$ {self.price} - toppings: {self.amount_toppings}'
    
#Cada item agregado pertence a una orden
#y ese item es un producto(pizza)
class Item_sale(models.Model):
    id_item_sale=models.AutoField(primary_key=True)
    #Establecer relaciones
    id_product=models.ForeignKey(Product,on_delete=models.CASCADE)
    id_orden=models.ForeignKey(Orden,on_delete=models.CASCADE)#Cada item pertence a una orden 
    amount=models.IntegerField(blank=True,null=True)
    details=models.CharField(max_length=200, blank=True, null=True)