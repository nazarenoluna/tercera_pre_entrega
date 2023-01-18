from datetime import date


from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from AppCoder.models import Estudiante, Profesor, Curso
from AppCoder.forms import CursoFormulario, ProfesorFormulario,EstudianteFormulario

# Creo mis vistas aqui
def inicio(request):
    return render(
        request=request,
        template_name='AppCoder/inicio.html',
    )


def listar_estudiantes(request):
    ## Aqui iria la validacion del permiso lectura estudiantes
    contexto = {
        'estudiantes': Estudiante.objects.all()
    }
    return render(
        request=request,
        template_name='AppCoder/lista_estudiantes.html',
        context=contexto,
    )


def listar_profesores(request):
    contexto = {
        'profesores': Profesor.objects.all()
    }
    return render(
        request=request,
        template_name='AppCoder/lista_profesores.html',
        context=contexto,
    )


def listar_cursos(request):
    contexto = {
        'cursos': Curso.objects.all()
    }
    return render(
        request=request,
        template_name='AppCoder/lista_cursos.html',
        context=contexto,
    )


def crear_curso(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso = Curso(nombre=data['nombre'],comision=data['comision'])
            curso.save()
            url_exitosa = reverse('listar_cursos')
            return redirect(url_exitosa)
        
    else:  # GET
        formulario = CursoFormulario()
        return render(
            request=request,
            template_name='AppCoder/formulario_curso.html',
            context={'formulario': formulario},
        ) 


def buscar_cursos(request):
    if request.method == "POST":
        data = request.POST
        cursos = Curso.objects.filter(nombre__contains=data['nombre']) 
        contexto ={
            'cursos': cursos
        }
        return render(
            request=request,
            template_name='AppCoder/busqueda_curso.html',
            context=contexto,
        )

def agregar_profesores(request):
    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso = Profesor(nombre=data['nombre'],apellido=data['apellido'],profesion=data['profesion'])
            curso.save()
            url_exitosa = reverse('listar_profesores')
            return redirect(url_exitosa)
        else:
            formulario = ProfesorFormulario()
            return render(
                request=request,
                template_name='AppCoder/formulario_profesores.html',
                context={'formulario': formulario},
            )
    else:  # GET
        formulario = ProfesorFormulario()
        return render(
            request=request,
            template_name='AppCoder/formulario_profesores.html',
            context={'formulario': formulario},
        ) 


def agregar_alumnos(request):
    if request.method == "POST":
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso = Estudiante(nombre=data['nombre'],apellido=data['apellido'],email=data['email'])
            curso.save()
            url_exitosa = reverse('listar_alumnos')
            return redirect(url_exitosa)
        else:
            formulario = EstudianteFormulario()
            return render(
                request=request,
                template_name='AppCoder/formulario_estudiante.html',
                context={'formulario': formulario},
            )
    else:  # GET
        formulario = EstudianteFormulario()
        return render(
            request=request,
            template_name='AppCoder/formulario_estudiante.html',
            context={'formulario': formulario},
        ) 
    
        