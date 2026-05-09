from django.urls import path
from django.contrib.auth.views import PasswordChangeView
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='Login'),
    path('logout/', views.CustomLogoutView.as_view(), name='Logout'),
    path('registro/', views.registro, name='Registro'),
    path('perfil/', views.ver_perfil, name='Perfil'),
    path('perfil/editar/', views.editar_perfil, name='EditarPerfil'),
    
    # Nueva ruta para cambiar la contraseña
    path('perfil/cambiar-password/', PasswordChangeView.as_view(template_name='accounts/cambiar_password.html', success_url='/accounts/perfil/'), name='CambiarPassword'),
]