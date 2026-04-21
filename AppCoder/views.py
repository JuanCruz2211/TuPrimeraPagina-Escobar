from django.shortcuts import render
from AppCoder.models import Curso, Estudiante, Profesor
from AppCoder.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario

def inicio(request):
    return render(request, "AppCoder/index.html")

def cursoFormulario(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST) 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["nombre"], camada=informacion["camada"])
            curso.save()
            return render(request, "AppCoder/index.html") 
    else:
        miFormulario = CursoFormulario()
    return render(request, "AppCoder/curso_formulario.html", {"miFormulario": miFormulario})

def estudianteFormulario(request):
    if request.method == "POST":
        miFormulario = EstudianteFormulario(request.POST) 
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=info["nombre"], apellido=info["apellido"], email=info["email"])
            estudiante.save()
            return render(request, "AppCoder/index.html") 
    else:
        miFormulario = EstudianteFormulario()
    return render(request, "AppCoder/estudiante_formulario.html", {"miFormulario": miFormulario})

def profesorFormulario(request):
    if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST) 
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            profesor = Profesor(nombre=info["nombre"], apellido=info["apellido"], email=info["email"], profesion=info["profesion"])
            profesor.save()
            return render(request, "AppCoder/index.html") 
    else:
        miFormulario = ProfesorFormulario()
    return render(request, "AppCoder/profesor_formulario.html", {"miFormulario": miFormulario})

def busquedaCurso(request):
    return render(request, "AppCoder/busqueda_curso.html")

def buscar(request):
    if request.GET.get("camada"):
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, "AppCoder/resultados_busqueda.html", {"cursos": cursos, "camada": camada})
    else:
        return render(request, "AppCoder/busqueda_curso.html", {"error": "No enviaste datos"})