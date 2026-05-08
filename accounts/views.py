from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .forms import RegistroFormulario, UserEditForm, PerfilEditForm
from .models import Perfil

def registro(request):
    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
    else:
        form = RegistroFormulario()
    return render(request, 'accounts/registro.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    next_page = 'Inicio'

class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
    next_page = 'Login'

@login_required
def ver_perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    return render(request, 'accounts/perfil.html', {'perfil': perfil})

@login_required
def editar_perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        perfil_form = PerfilEditForm(request.POST, request.FILES, instance=perfil)
        
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            return redirect('Perfil')
    else:
        user_form = UserEditForm(instance=request.user)
        perfil_form = PerfilEditForm(instance=perfil)
        
    return render(request, 'accounts/editar_perfil.html', {'user_form': user_form, 'perfil_form': perfil_form})