from django.shortcuts import render, redirect  
from django.http import HttpResponse
from django.contrib import messages

from .import forms 
from .forms import alta_autosForm
# Otra opcion: from .forms import * (y se le quita forms abajo)

# Create your views here.
def index(request):
    # Accedo a la BBDD a traves de los modelos
    return render(request, 'rentacars/index.html')

def listado_autos(request):
    contexto = {}
    return render(request, 'rentacars/listado_autos.html', contexto)

def alta_autos(request):
    contexto = {}
    if request.method == "GET":
        contexto['alta_autos_form'] = alta_autosForm()
    else:
        form = alta_autosForm(request.POST)
        contexto['alta_autos_form'] = form  
        # Validar el formulario
        if form.is_valid():
            messages.success(request, 'El Auto fue dado de alta con éxito')
            return redirect('alta_autos')
    return render(request, 'rentacars/alta_autos.html', contexto)

def nosotros(request):
    contexto = {}
    return render(request, 'rentacars/nosotros.html', contexto)

def contacto(request):
    contexto = {}
    return render(request, 'rentacars/contacto.html', contexto)

def login(request):
    contexto = {
        'login_form' : forms.LoginForm()
    }
    return render(request, 'rentacars/login.html', contexto)

def perdiste_Contraseña(request):
    contexto = {
        'perdiste_Contraseña_form' : forms.Perdiste_ContraseñaForm()
    }
    return render(request, 'rentacars/perdiste_Contraseña.html', contexto)

def registrarse(request):
    contexto = {
        'registrarse_form' : forms.RegistrarseForm()
    }
    return render(request, 'rentacars/registrarse.html', contexto)