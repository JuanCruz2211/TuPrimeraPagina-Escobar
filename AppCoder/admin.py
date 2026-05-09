from django.contrib import admin
from .models import Estudiante, Profesor, Curso, Entregable, Articulo, Mensaje

# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Entregable)
admin.site.register(Articulo)
admin.site.register(Mensaje)