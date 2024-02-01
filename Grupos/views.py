from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib import messages
from .models import Grupo, Estudiante, Asignatura, Asignatura_Estudiante
from .forms import EstudianteForm
from .forms import AsignaturaForm

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Si el usuario es autenticado correctamente, inicia sesión y redirige a la página de inicio
            login(request, user)
            return redirect("home")
        else:
            # Si el usuario no es autenticado, muestra un mensaje de error en el formulario
            messages.error(request, "Usuario o contraseña incorrectos.")
    return render(request, "login.html")

def cerrar_sesion(request):
    logout(request)
    return redirect('login')
@login_required(login_url="login")
def home(request):
    return render(request, "home.html")

@login_required(login_url="login")
def crear_grupo(request):
    error_message = None

    if request.method == 'POST':
        año = request.POST['año']

        if len(año) != 4 or not año.isdigit():
            error_message = "El año debe contener 4 cifras numéricas."
        elif not (año.startswith('19') or año.startswith('20')):
            error_message = "Las dos primeras cifras del año deben ser 19 o 20."
        else:
            try:
                Grupo.objects.create(año=año)
                return redirect('lista_grupos')
            except IntegrityError:
                error_message = "El grupo con ese año ya existe."

    return render(request, 'crear_grupo.html', {'error_message': error_message})

@login_required(login_url="login")
def lista_grupos(request):
    grupos = Grupo.objects.all()
    return render(request, 'lista_grupos.html', {'grupos': grupos})

@login_required(login_url="login")
def agregar_estudiante(request, grupo_id):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        grupo = Grupo.objects.get(pk=grupo_id)
        Estudiante.objects.create(nombre=nombre, apellido=apellido, direccion=direccion, telefono=telefono, grupo_año=grupo)
        return redirect('detalle_grupo', grupo_id=grupo_id)
    return render(request, 'agregar_estudiante.html', {'grupo_id': grupo_id})

@login_required(login_url="login")
def detalle_grupo(request, grupo_id):
    grupo = Grupo.objects.get(pk=grupo_id)
    estudiantes = Estudiante.objects.filter(grupo_año=grupo)
    return render(request, 'detalle_grupo.html', {'grupo': grupo, 'estudiantes': estudiantes})

@login_required(login_url="login")
def agregar_nota(request, estudiante_id):
    asignaturas = Asignatura.objects.all()
    if request.method == 'POST':
        asginatura_id = request.POST['asignatura']
        print(asginatura_id)
        nota = request.POST['nota']
        estudiante = Estudiante.objects.get(pk=estudiante_id)
        asignatura = Asignatura.objects.get(pk=asginatura_id)
        Asignatura_Estudiante.objects.create(estudiante_id_estudiante= estudiante, asignatura_name=asignatura , nota=nota)
        return redirect('detalle_estudiante', estudiante_id=estudiante_id)
    return render(request, 'agregar_nota.html', {'estudiante_id': estudiante_id, 'asignaturas': asignaturas})

@login_required(login_url="login")
def detalle_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, pk=estudiante_id)
    asignaturas = Asignatura_Estudiante.objects.filter(estudiante_id_estudiante=estudiante_id)
    return render(request, 'detalle_estudiante.html', {'estudiante': estudiante, 'asignaturas': asignaturas})

@login_required(login_url="login")
def modificar_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, pk=estudiante_id)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            direccion = form.cleaned_data['direccion']
            telefono = str(form.cleaned_data['telefono'])  # Convertir telefono a una cadena

            # Validar que el nombre y el apellido no contengan números
            if any(char.isdigit() for char in nombre) or any(char.isdigit() for char in apellido):
                form.add_error('nombre', 'El nombre y el apellido no deben contener números.')

            # Validar que el campo de direccion no esté vacío
            if not direccion:
                form.add_error('direccion', 'Por favor, introduce una dirección.')

            # Validar que el campo de telefono contenga exactamente 8 dígitos numéricos
            if not telefono.isdigit() or len(telefono) != 8:
                form.add_error('telefono', 'El teléfono debe contener 8 números.')

            if not form.errors:  # Si no hay errores de validación adicionales
                form.save()
                return redirect('detalle_estudiante', estudiante_id=estudiante_id)
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'modificar_estudiante.html', {'form': form, 'estudiante': estudiante})

@login_required(login_url="login")
def eliminar_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, pk=estudiante_id)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('lista_grupos')
    return render(request, 'eliminar_estudiante.html', {'estudiante': estudiante})

@login_required(login_url="login")
def eliminar_grupo(request, grupo_id):
    grupo = get_object_or_404(Grupo, pk=grupo_id)
    grupo.delete()
    return redirect('lista_grupos')

@login_required(login_url="login")
def agregar_asignatura(request):
    if request.method == 'POST':
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_asignatura')  # Redirige a la página de lista de asignaturas
    else:
        form = AsignaturaForm()

    asignaturas = Asignatura.objects.all()  # Obtiene todos los elementos de Asignatura
    return render(request, 'agregar_asignatura.html', {'form': form, 'asignaturas': asignaturas})

@login_required(login_url="login")
def gestor_notas_view(request):
    # Lógica de la vista aquí
    return render(request, 'about.html')

@login_required(login_url="login")
def admin_view(request):
    return redirect('admin.site.urls')

@login_required(login_url="login")
def modificar_asignatura(request, nombre):
    asignatura = Asignatura.objects.get(nombre=nombre)
    if request.method == 'POST':
        form = AsignaturaForm(request.POST, instance=asignatura)
        if form.is_valid():
            form.save()
            return redirect('agregar_asignatura')
    else:
        form = AsignaturaForm(instance=asignatura)
    
    asignaturas = Asignatura.objects.all()
    return render(request, 'agregar_asignatura.html', {'form': form, 'asignaturas': asignaturas, 'asignatura_modificar': asignatura})

@login_required(login_url="login")
def eliminar_asignatura(request, nombre):
    asignatura = Asignatura.objects.get(nombre=nombre)
    asignatura.delete()
    return redirect('agregar_asignatura')


def eliminar_nota(request, asignatura_id):
    asignatura_estudiante = get_object_or_404(Asignatura_Estudiante, pk=asignatura_id)
    estudiante_id = asignatura_estudiante.estudiante_id_estudiante.pk
    asignatura_estudiante.delete()
    return redirect('detalle_estudiante', estudiante_id=estudiante_id)
