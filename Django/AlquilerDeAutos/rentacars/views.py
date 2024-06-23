import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .import forms 
from .forms import alta_autosForm
from .models import Auto, Usuario, Alquiler
from .forms import AlquilerForm
from .forms import RegistrarseForm
from django.contrib.auth import login, logout


# Otra opcion: from .forms import * (y se le quita forms abajo)

# Create your views here.

def obtener_autos():
    autos = Auto.objects.all()
    contexto = {'autos': autos}
    return contexto

def get_precio_diario(request, id):
    auto = get_object_or_404(Auto, id=id)
    data = {
        'precio_diario': str(auto.precio)
    }
    return JsonResponse(data)

def index(request):
    contexto = obtener_autos()
    return render(request, 'rentacars/index.html', contexto)

def usuario_logout(request):
    logout(request)
    return render(request, 'login')

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
            messages.success(request, 'El Auto fue dado de alta con éxito')
            nuevo_auto = Auto(
                marca=form.cleaned_data['marca'],
                modelo=form.cleaned_data['modelo'],
                color=form.cleaned_data['color'],
                patente=form.cleaned_data['patente'],
                precio=form.cleaned_data['precio'],
                imagen=form.cleaned_data['imagen'])
            nuevo_auto.save()

            return redirect('alta_autos')

    return render(request, 'rentacars/alta_autos.html', contexto)


# def alquiler_autos(request):
#     contexto = {}
#     if request.method == "GET":
#         contexto['alquiler_autos_form'] = alquiler_autosForm()
#     else:
#         form = alquiler_autosForm(request.POST)
#         contexto['alquiler_autos_form'] = form
#         # Validar el formulario
#         if form.is_valid():
#             messages.success(request, 'El Alquiler fue registrado con éxito')
#             precio_diario = Auto.objects.get(id=form.cleaned_data['auto'].id).precio
#             dias = form.cleaned_data['fecha_fin'] - form.cleaned_data['fecha_inicio']
#             nuevo_alquiler = Alquiler(
#                 auto=form.cleaned_data['auto'],
#                 usuario=form.cleaned_data['usuario'],
#                 fecha_inicio=form.cleaned_data['fecha_inicio'],
#                 fecha_fin=form.cleaned_data['fecha_fin'],
#                 precio_total= precio_diario * (dias.days + 1)
#             )
#             nuevo_alquiler.save()
#
#             return redirect('alquiler_autos')
#
#     return render(request, 'rentacars/alquiler_autos.html', contexto)

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

@login_required()
def crear_alquiler(request, auto_id):
    auto = get_object_or_404(Auto, id=auto_id)
    if request.method == 'POST':
        form = AlquilerForm(request.POST)
        if form.is_valid():
            dias = form.cleaned_data['fecha_fin'] - form.cleaned_data['fecha_inicio']
            alquiler = form.save(commit=False)
            usuario_auth = request.user
            try:
                usuario = Usuario.objects.get(user=usuario_auth)
                alquiler.usuario = usuario
                alquiler.auto = auto
                alquiler.precio_total = auto.precio * (dias.days + 1)
                alquiler.save()
                messages.success(request, 'Alquiler creado con éxito.')
                return redirect('listado_alquileres')
            except Usuario.DoesNotExist:
                messages.error(request, 'Usuario no encontrado.')
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
    contexto = {}
    return render(request, 'rentacars/contacto.html', contexto)

def perdiste_Contraseña(request):
    contexto = {
        'perdiste_Contraseña_form': forms.Perdiste_ContraseñaForm()
    }
    return render(request, 'rentacars/perdiste_Contraseña.html', contexto)
