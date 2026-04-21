from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('agregar-curso/', views.cursoFormulario, name="CursoFormulario"),
    path('agregar-estudiante/', views.estudianteFormulario, name="EstudianteFormulario"),
    path('agregar-profesor/', views.profesorFormulario, name="ProfesorFormulario"),
    path('busqueda-curso/', views.busquedaCurso, name="BusquedaCurso"),
    path('buscar/', views.buscar, name="Buscar"),
]