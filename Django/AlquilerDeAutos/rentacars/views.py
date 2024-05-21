from django.shortcuts import render
from django.http import HttpResponse

from .import forms 
# Otra opcion: from .forms import * (y se le quita forms abajo)

# Create your views here.
def index(request):
    # Accedo a la BBDD a traves de los modelos

    return render(request, 'rentacars/index.html')


def listado_autos(request):

    contexto = {}

    return render(request, 'rentacars/listado_autos.html', contexto)

def alta_auto(request):
    
    contexto = {}

    return render(request, 'rentacars/alta_autos.html', contexto)

def nosotros(request):
    
    contexto = {}

    return render(request, 'rentacars/nosotros.html', contexto)

def contacto(request):
    
    contexto = {}

    return render(request, 'rentacars/contacto.html', contexto)

def loguin(request):
    contexto = {
        'loguin_form' : forms.LoguinForm()
    }
    return render(request, 'rentacars/loguin.html', contexto)

def perdisteContraseña(request):
    contexto = {
        'perdisteContraseña_form' : forms.ContraseñaForm()
    }
    return render(request, 'rentacars/perdisteContraseña.html', contexto)

def registrarse(request):
    contexto = {
        'registrarse_form' : forms.RegistrarseForm()
    }
    return render(request, 'rentacars/registrarse.html', contexto)