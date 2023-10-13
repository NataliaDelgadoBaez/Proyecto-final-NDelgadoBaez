from django.urls import path
from Tienda_app import views

urlpatterns = [
    
    path('inicio/', views.inicio, name="Inicio"),
    path('tienda/', views.tienda, name="Tienda"),
    path('blog/', views.blog, name="Blog"),
    path('busca tu favorito/', views.Buscar_album, name="Busca tu favorito"),
    path('mostra tu favorito/', views.Mostraralbum, name="Mostra tu favorito"),
    path('carrito/', views.carrito, name="Carrito"),
    path('destacados/', views.destacados, name="Destacados"),
    path('ingresa/', views.iniciar_sesion, name="Ingresa"),
    path('soy nuevo/', views.crear_cuenta, name="Soy nuevo"),
    path('tu opinion/', views.tu_opinion, name="Tu opinion"),
    path('crear album/', views.Agregaralbum, name="Crear album"),
    path('musica de siempre/', views.musica_siempre, name="Musica de siempre"),
    path('musica de hoy/', views.musica_hoy, name="Musica de hoy"),
    path('entrevistas/', views.entrevistas, name="Entrevistas"),
    path('conocenos/', views.conocenos, name="Conocenos"),
    
]
