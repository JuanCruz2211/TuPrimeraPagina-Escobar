from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('agregar-curso/', views.cursoFormulario, name="CursoFormulario"),
    path('agregar-estudiante/', views.estudianteFormulario, name="EstudianteFormulario"),
    path('agregar-profesor/', views.profesorFormulario, name="ProfesorFormulario"),
    path('busqueda-curso/', views.busquedaCurso, name="BusquedaCurso"),
    path('buscar/', views.buscar, name="Buscar"),

    path('pages/', views.ArticuloListView.as_view(), name='Articulos'),
    path('pages/nuevo/', views.ArticuloCreateView.as_view(), name='ArticuloCrear'),
    path('pages/<int:pk>/', views.ArticuloDetailView.as_view(), name='ArticuloDetalle'),
    path('pages/editar/<int:pk>/', views.ArticuloUpdateView.as_view(), name='ArticuloEditar'),
    path('pages/borrar/<int:pk>/', views.ArticuloDeleteView.as_view(), name='ArticuloBorrar'),
    
    path('about/', views.about, name='About'),
    path('mensajes/', views.mensajeria, name='Mensajeria'),
]