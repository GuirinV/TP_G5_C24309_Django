import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from .import forms 
from .forms import alta_autosForm
from .models import Auto, Usuario, Alquiler
from .forms import AlquilerForm
from .forms import RegistrarseForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy

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
    # Accedo a la BBDD a traves de los modelos
    return render(request, 'rentacars/index.html', contexto)

def usuario_logout(request):
    logout(request)
    return render(request, 'login')

@login_required
@user_passes_test(lambda u: u.is_staff,login_url=reverse_lazy('permission_denied'))
def listado_autos(request):
    contexto = obtener_autos()
    return render(request, 'rentacars/listado_autos.html', contexto)

@login_required
@user_passes_test(lambda u: u.is_staff,login_url=reverse_lazy('permission_denied'))
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
    return render(request, 'rentacars/listado_autos.html')

@login_required
@user_passes_test(lambda u: u.is_staff,login_url=reverse_lazy('permission_denied'))
def eliminar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)
    if request.method == 'POST':
        auto.delete()
        messages.success(request, 'Auto eliminado con éxito.')
        return redirect('listado_autos')
    return render(request, 'rentacars/listado_autos.html')

@login_required
@user_passes_test(lambda u: u.is_staff,login_url=reverse_lazy('permission_denied'))
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



def registrarse(request):
    contexto = {}
    if request.method == "GET":
        contexto['Registrarse_Form'] = RegistrarseForm()
    else:
        form = RegistrarseForm(request.POST)
        contexto['Registrarse_Form'] = form
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['nombre'],  
                last_name=form.cleaned_data['apellido'] 
            )
            nuevo_usuario = Usuario(
                user=user,
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                cuit=form.cleaned_data['cuit'],
                direccion=form.cleaned_data['direccion'],
                telefono=form.cleaned_data['telefono']
            )
            nuevo_usuario.save()
            login(request, user)  # Iniciar sesión automáticamente
            return redirect('index')
    return render(request, 'rentacars/registrarse.html', contexto)

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
    usuario_auth = request.user  # Esto es una instancia del modelo User
    try:
        usuario = Usuario.objects.get(user=usuario_auth)
        alquileres = Alquiler.objects.filter(usuario=usuario)
        context = {'alquileres': alquileres}
        return render(request, 'rentacars/listado_alquileres.html', context)
    except Usuario.DoesNotExist:
        messages.error(request, 'Usuario no encontrado.')
        return redirect('index')


@login_required
def editar_alquiler(request, alquiler_id):
    alquiler = get_object_or_404(Alquiler, id=alquiler_id)
    auto = get_object_or_404(Auto, id=alquiler.auto_id)

    if request.method == 'POST':
        form = AlquilerForm(request.POST, instance=alquiler)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alquiler actualizado con éxito.')
            return redirect('listado_alquileres')
    else:
        form = AlquilerForm(instance=alquiler)

    return render(request, 'rentacars/editar_alquiler.html', {'form': form, 'auto': auto})

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


@login_required
def permission_denied_view(request):
    messages.error(request, 'No tienes permisos para acceder a esta página.')
    return redirect('index')