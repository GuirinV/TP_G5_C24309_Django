from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages

from .import forms 
from .forms import alta_autosForm
from  .models import Auto
# Otra opcion: from .forms import * (y se le quita forms abajo)

# Create your views here.

def obtener_autos():
    autos = Auto.objects.all()
    contexto = {'autos': autos}
    return contexto

def index(request):
    contexto = obtener_autos()
    # Accedo a la BBDD a traves de los modelos
    return render(request, 'rentacars/index.html', contexto)

def listado_autos(request):
    contexto = obtener_autos()
    return render(request, 'rentacars/listado_autos.html', contexto)

def editar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)
    if request.method == 'POST':
        auto.marca = request.POST['marca']
        auto.modelo = request.POST['modelo']
        auto.color = request.POST['color']
        auto.precio = request.POST['precio']
        auto.imagen = request.POST['imagen']
        auto.save()
        return redirect('listado_autos')
    return render(request, 'rentacars/listado_autos.html')

def eliminar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)
    if request.method == 'POST':
        auto.delete()
        return redirect('listado_autos')
    return render(request, 'rentacars/listado_autos.html')

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
            nuevo_auto  = Auto(
                marca=form.cleaned_data['marca'],
                modelo=form.cleaned_data['modelo'],
                color=form.cleaned_data['color'],
                patente=form.cleaned_data['patente'],
                precio=form.cleaned_data['precio'],
                imagen = form.cleaned_data['imagen'] )
            nuevo_auto.save()

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