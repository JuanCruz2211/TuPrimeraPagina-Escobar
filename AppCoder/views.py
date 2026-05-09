from django.shortcuts import render, redirect
from AppCoder.models import Curso, Estudiante, Profesor, Articulo, Mensaje
from AppCoder.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# --- Vistas Generales ---

def inicio(request):
    return render(request, "AppCoder/index.html")

def about(request):
    return render(request, 'AppCoder/about.html')

# --- Formularios de Registro ---

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

# --- Búsqueda ---

def busquedaCurso(request):
    return render(request, "AppCoder/busqueda_curso.html")

def buscar(request):
    if request.GET.get("camada"):
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, "AppCoder/resultados_busqueda.html", {"cursos": cursos, "camada": camada})
    else:
        return render(request, "AppCoder/busqueda_curso.html", {"error": "No enviaste datos"})
    
# --- Vistas del Blog (CBV) ---

class ArticuloListView(ListView):
    model = Articulo
    template_name = "AppCoder/articulo_list.html"

class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = "AppCoder/articulo_detail.html"

class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
    template_name = "AppCoder/articulo_form.html"
    success_url = reverse_lazy('Articulos')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
    template_name = "AppCoder/articulo_form.html"
    success_url = reverse_lazy('Articulos')

class ArticuloDeleteView(LoginRequiredMixin, DeleteView):
    model = Articulo
    template_name = "AppCoder/articulo_confirm_delete.html"
    success_url = reverse_lazy('Articulos')

# --- Mensajería ---

@login_required
def mensajeria(request):
    mensajes = Mensaje.objects.filter(receptor=request.user).order_by('-fecha')
    return render(request, 'AppCoder/mensajeria.html', {'mensajes': mensajes})