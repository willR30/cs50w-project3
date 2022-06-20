from django.contrib import admin
from .models import  Category,State,Orden, Item_sale,Type,Product #importamos nuestro modelo desde el archivo fuente
# Register your models here.

# Register your models here.

#Agregamos el modelo al panel de administración
admin.site.register(State)
admin.site.register(Category)

admin.site.register(Orden)
admin.site.register(Item_sale)
admin.site.register(Type)
admin.site.register(Product)
