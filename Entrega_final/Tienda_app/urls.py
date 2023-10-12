from django.urls import path
from Tienda_app import views

urlpatterns = [
    
    path('inicio/', views.inicio),
    path('tienda/', views.tienda, name="Tienda"),
    path('discos_comprados/', views.discos_comprados),
    path('disco_vendidos/', views.discos_vendidos),
    path('usuarios/', views.usuarios),
    path('iniciar_sesion/', views.iniciar_sesion),
    path('crear_cuenta/', views.crear_cuenta),
    path('Discform/', views.Discoforms, name="Discoforms"),
    path('Buscar/', views.Buscardisco, name="Buscardisco"),
    
]
