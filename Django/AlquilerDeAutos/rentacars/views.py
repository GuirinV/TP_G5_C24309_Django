from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . import forms
from .forms import alta_autosForm, AlquilerForm, RegistrarseForm
from .models import Auto, Usuario, Alquiler
from django.contrib.auth import login

# Función para obtener autos
def obtener_autos():
    autos = Auto.objects.all()
    return {'autos': autos}

# Vistas
def index(request):
    contexto = obtener_autos()
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
        messages.success(request, 'Auto actualizado con éxito.')
        return redirect('listado_autos')
    return render(request, 'rentacars/editar_auto.html', {'auto': auto})

def eliminar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)
    if request.method == 'POST':
        auto.delete()
        messages.success(request, 'Auto eliminado con éxito.')
        return redirect('listado_autos')
    return render(request, 'rentacars/eliminar_auto.html', {'auto': auto})

def alta_autos(request):
    if request.method == "GET":
        form = alta_autosForm()
    else:
        form = alta_autosForm(request.POST)
        if form.is_valid():
            nuevo_auto = form.save()
            messages.success(request, 'El Auto fue dado de alta con éxito.')
            return redirect('listado_autos')
    return render(request, 'rentacars/alta_autos.html', {'alta_autos_form': form})

def registrarse(request):
    if request.method == "GET":
        form = RegistrarseForm()
    else:
        form = RegistrarseForm(request.POST)
        if form.is_valid():
            user = form.save()
            Usuario.objects.create(user=user, **form.cleaned_data)
            login(request, user)
            messages.success(request, 'Registro exitoso. Bienvenido!')
            return redirect('index')
    return render(request, 'rentacars/registrarse.html', {'Registrarse_Form': form})

@login_required
def crear_alquiler(request, auto_id):
    auto = get_object_or_404(Auto, id=auto_id)
    if request.method == 'POST':
        form = AlquilerForm(request.POST)
        if form.is_valid():
            alquiler = form.save(commit=False)
            alquiler.usuario = Usuario.objects.get(user=request.user)
            alquiler.auto = auto
            alquiler.save()
            messages.success(request, 'Alquiler creado con éxito.')
            return redirect('listado_alquileres')
        else:
            messages.error(request, 'Formulario no válido. Por favor, verifica los datos ingresados.')
    else:
        form = AlquilerForm()
    return render(request, 'rentacars/crear_alquiler.html', {'form': form, 'auto': auto})

@login_required
def listado_alquileres(request):
    alquileres = Alquiler.objects.all()
    return render(request, 'rentacars/listado_alquileres.html', {'alquileres': alquileres})

@login_required
def editar_alquiler(request, alquiler_id):
    alquiler = get_object_or_404(Alquiler, id=alquiler_id)
    if request.method == 'POST':
        form = AlquilerForm(request.POST, instance=alquiler)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alquiler actualizado con éxito.')
            return redirect('listado_alquileres')
    else:
        form = AlquilerForm(instance=alquiler)
    return render(request, 'rentacars/editar_alquiler.html', {'form': form})

@login_required
def eliminar_alquiler(request, alquiler_id):
    alquiler = get_object_or_404(Alquiler, id=alquiler_id)
    if request.method == 'POST':
        alquiler.delete()
        messages.success(request, 'Alquiler eliminado con éxito.')
        return redirect('listado_alquileres')
    return render(request, 'rentacars/eliminar_alquiler.html', {'alquiler': alquiler})

def nosotros(request):
    return render(request, 'rentacars/nosotros.html')

def contacto(request):
    return render(request, 'rentacars/contacto.html')

def perdiste_Contraseña(request):
    contexto = {
        'perdiste_Contraseña_form': forms.Perdiste_ContraseñaForm()
    }
    return render(request, 'rentacars/perdiste_Contraseña.html', contexto)
