from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='Login'),
    path('logout/', views.CustomLogoutView.as_view(), name='Logout'),
    path('registro/', views.registro, name='Registro'),
]