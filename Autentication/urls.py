from django import views
from django.urls import path
from . import views
#aqui debo de gestionar las rutas de las paguinas web que quiero mostrar
urlpatterns = [
    #La funcion de login se mantiene pero en el  "login" de Django se cambia el nombre
    path('', views.login,name='login'),
    path('register', views.register,name='register'), #Son los nombres identifiacodores de las funciones desde las vistas
    path('user_logout',views.user_logout,name='user_logout')

]