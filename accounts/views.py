from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegistroFormulario
# Create your views here.

def registro(request):
    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login') # Lo enviamos a iniciar sesión tras registrarse
    else:
        form = RegistroFormulario()
    return render(request, 'accounts/registro.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    next_page = 'Inicio' # A dónde va después de loguearse

class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
    next_page = 'Login' # A dónde va al cerrar sesión