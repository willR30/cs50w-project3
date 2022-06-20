from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , logout
from django.contrib.auth import login as login_django_funcion #cambiamos el import de la funcion propia de django
from Pizza.views import home #importamos la vista principal de la aplicacion de pizza
# Create your views here.


def login(request):
    #Validamos si el usuario ya inició sesion en nuestro sitio
    if request.method =='POST':
        #Capturamos los valores
        username=request.POST['txt_user']
        password=request.POST['txt_password']
        #validamos campos nulos
        if username is None or password is None:
            print("No se admiten campos nulos")
        else:
            user = authenticate(username = username, password = password)
            if user is not None:
                print("Autenticado")

                login_django_funcion(request,user)
                messages.success(request, 'Bienvenido!.')
                print("Logeado")
                #nos redireccionamos al home 
                return redirect(to="home")
            else:
                print("Cotrasela mala")
                messages.success(request, 'Usuario o contraseña incorrecta.')
                return redirect(to='login')

    else:
        #validamos si ya estamos autenticados
        if request.user.is_authenticated:
            return redirect("home")   
        else:
            return render(request,'login.html')



def register(request):
    #validamos el metodo post
    if request.method == 'POST':
        #capturamos los valores 
        firstname = request.POST['txt_name']
        lastname = request.POST['txt_last_name']
        username = request.POST['txt_user_name']
        email = request.POST['txt_email']
        password = request.POST['password']
        password2 = request.POST['confirm_password']

        #validamos las contraseñas
        if password == password2:
            #Validamos si el usuario existe
            if User.objects.filter(username=username).exists():
                messages.success(request, 'El usuario ya existe!.')
                return render(request, 'register.html')
            
            #Validamos si el correo ya existe
            elif User.objects.filter(email=email).exists():
                    messages.success(request, 'El correo ya existe!.')
                    return render(request, 'register.html')
            else:
                #si todo está bien , procedemos a crear el usuario
                user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
                user.save()
                messages.success(request, 'Bienvenido!.')
                return render(request, 'login.html')
        else:
            return render(request, 'register.html')

    else:
        return render(request,'register.html')

#Logout
def user_logout(request):
    logout(request)
    return redirect('login')