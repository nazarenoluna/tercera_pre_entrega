from django.urls import path

from AppCoder.views import (
    listar_estudiantes, listar_profesores, listar_cursos,
    crear_curso, buscar_cursos, agregar_profesores, agregar_alumnos
)


urlpatterns = [
    path('alumnos/', listar_estudiantes, name="listar_alumnos") ,
    path('profesores/', listar_profesores, name="listar_profesores") ,
    path('cursos/', listar_cursos, name="listar_cursos"),
    path('crear-curso/', crear_curso, name="crear_curso"),
    path('buscar-cursos/', buscar_cursos, name="buscar_cursos"),
    path('agregar-profesores/', agregar_profesores, name="agregar_profesores"),
    path('agregar-alumnos/', agregar_alumnos, name="agregar_estudiantes"),
]