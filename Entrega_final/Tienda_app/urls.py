from django.urls import path
from Tienda_app import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('inicio/', views.inicio, name="Inicio"),
    path('tienda/', views.tienda, name="Tienda"),
    path('blog/', views.blog, name="Blog"),
    path('busca tu favorito/', views.Buscar_album, name="Busca tu favorito"),
    path('mostra tu favorito/', views.Mostraralbum, name="Mostra tu favorito"),
    path('carrito/', views.carrito, name="Carrito"),
    path('carrito/', views.final_carrito, name="Fcarrito"),
    path('destacados/', views.destacados, name="Destacados"),
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Soy nuevo"),
    path('logout/', LogoutView.as_view(template_name='Tienda_app/logout.html'), name="Logout"),
    path('tu opinion/', views.tu_opinion, name="Tu opinion"),
    path('crear album/', views.Agregaralbum, name="Crear album"),
    path('musica de siempre/', views.musica_siempre, name="Musica de siempre"),
    path('musica de hoy/', views.musica_hoy, name="Musica de hoy"),
    path('entrevistas/', views.entrevistas, name="Entrevistas"),
    path('conocenos/', views.conocenos, name="Conocenos"),
    
]
