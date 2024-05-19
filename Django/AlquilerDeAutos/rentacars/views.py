from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # Accedo a la BBDD a traves de los modelos

    return render(request, 'rentacars/index.html')


def listado_autos(request):

    contexto = {}

    return render(request, 'rentacars/listado_alumnos.html', contexto)

def alta_auto(request):
    
    contexto = {}

    return render(request, 'rentacars/alta_auto.html', contexto)

def nosotros(request):
    
    contexto = {}

    return render(request, 'rentacars/nosotros.html', contexto)

def contacto(request):
    
    contexto = {}

    return render(request, 'rentacars/contacto.html', contexto)