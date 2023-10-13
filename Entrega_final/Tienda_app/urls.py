from django.urls import path
from Tienda_app import views

urlpatterns = [
    
    path('inicio/', views.inicio),
    path('tienda/', views.tienda, name="Tienda"),
    path('blog/', views.blog, name="Blog"),
    path('busca tu favorito/', views.busca_favorito, name="busca tu favorito"),
    path('carrito/', views.carrito, name="Carrito"),
    path('destacados/', views.tu_opinion, name="Tu opinion"),
    path('discos de siempre/', views.destacados, name="Destacados"),
    path('ingresa/', views.iniciar_sesion, name="ingresa"),
    path('soy nuevo/', views.crear_cuenta, name="Soy nuevo"),
    path('tu opinion/', views.tu_opinion, name="Tu opinion"),
    
]
