from django.urls import path
from . import views

urlpatterns = [
    path('', views.seleccion_procesadores, name='seleccion'),
    path('comparar/', views.comparar_procesadores, name='comparar'),
    path('login/', views.login_view, name='login'),  # Ruta para el inicio de sesión
]