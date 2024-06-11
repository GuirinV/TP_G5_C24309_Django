from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from .import forms 
from .forms import LoginForm, alta_autosForm
from  .models import Auto, Usuario
from .forms import AlquilerForm
from .forms import RegistrarseForm

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

def registrarse(request):
    contexto = {}
    if request.method == "GET":
        contexto['Registrarse_Form'] = RegistrarseForm()
    else:
        form = RegistrarseForm(request.POST)
        contexto['Registrarse_Form'] = form
        if form.is_valid():
            nuevo_usuario = Usuario(
                nombre=form.cleaned_data['Nombre'],
                apellido=form.cleaned_data['Apellido'],
                cuit=form.cleaned_data['CUIT'],
                direccion=form.cleaned_data['direccion'],
                telefono=form.cleaned_data['telefono'],
                email=form.cleaned_data['email'],
                usuario=form.cleaned_data['usuario'],
                password = form.cleaned_data['password']
            )
            nuevo_usuario.save()
            # Redirigir al usuario a una página de éxito o a cualquier otra página deseada
            return redirect('index')
    return render(request, 'rentacars/registrarse.html', contexto)

@login_required
def crear_alquiler(request, auto_id):
    auto = get_object_or_404(Auto, id=auto_id)
    usuario = request.user

    if request.method == 'POST':
        form = AlquilerForm(request.POST)
        if form.is_valid():
            alquiler = form.save(commit=False)
            alquiler.auto = auto
            alquiler.usuario = usuario
            alquiler.precio_total = (alquiler.fecha_fin - alquiler.fecha_inicio).days * auto.precio
            alquiler.save()
            return redirect('listado_alquileres')
    else:
        form = AlquilerForm(initial={'auto': auto, 'usuario': usuario})

    return render(request, 'rentacars/crear_alquiler.html', {'form': form, 'auto': auto, 'usuario': usuario})

def nosotros(request):
    contexto = {}
    return render(request, 'rentacars/nosotros.html', contexto)

def contacto(request):
    contexto = {}
    return render(request, 'rentacars/contacto.html', contexto)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['usename']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')  # Redirige a la página principal u otra página deseada
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    else:
        form = LoginForm()

    contexto = {'login_form': form}
    return render(request, 'rentacars/login.html', contexto)


def perdiste_Contraseña(request):
    contexto = {
        'perdiste_Contraseña_form' : forms.Perdiste_ContraseñaForm()
    }
    return render(request, 'rentacars/perdiste_Contraseña.html', contexto)
