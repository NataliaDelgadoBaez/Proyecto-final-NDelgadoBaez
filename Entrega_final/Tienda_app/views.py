from django.shortcuts import render
from Tienda_app.models import Disco
from Tienda_app.forms import Crearalbumform, Buscaralbumform



def inicio(request):
    return render(request, "Tienda_app/index.html")

def tienda(request):
    return render(request, "Tienda_app/tienda.html")

def blog(request):
    return render(request, "tienda_app/blog.html")

def busca_favorito(request):
    return render(request, "Tienda_app/busca tu favorito.html")

def carrito(request):
    return render(request, "Tienda_app/carrito.html")

def destacados(request):
    return render(request, "Tienda_app/destacados.html")

def iniciar_sesion(request):
    return render(request, "Tienda_app/ingresa.html")

def crear_cuenta(request):
    return render(request, "Tienda_app/soy nuevo.html")

def tu_opinion(request):
    return render(request, "Tienda_app/tu opinion.html")

def musica_siempre(request):
    return render(request, "Tienda_app/Musica de siempre.html")

def musica_hoy(request):
    return render(request, "Tienda_app/Musica de hoy.html")

def conocenos(request):
    return render(request, "Tienda_app/conocenos.html")

def entrevistas(request):
    return render(request, "Tienda_app/entrevistas.html")


def Agregaralbum (request):
 
    if request.method == "POST":
 
        miFormulario = Agregaralbum(request.POST) 
        print(miFormulario)
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            album=  Disco(nombre=request.POST['album'],autor=request.POST['artista'], año=request.POST['año'], precio=request.POST['precio'])
            album.save()
            return render(request, "Tienda_app/index.html")
    else:
            miFormulario = Crearalbumform()
 
            return render(request, "Tienda_app/agregar album.html", {"miFormulario": miFormulario})


def Buscar_album(request):
    if request.method == "POST":
        miFormulario = Buscaralbumform(request.POST) 

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            discos = Disco.objects.filter(nombre__icontains=informacion["album"])

            return render(request, "Tienda_app/mostra tu favorito.html", {"album": discos})
    else:
        miFormulario = Buscaralbumform()

    return render(request, "Tienda_app/busca tu favorito.html", {"miFormulario": miFormulario})

def Mostraralbum (request):

    discos = Disco.objects.all() 

    contexto= {"cursos":discos} 

    return render(request, "Tienda_app/mostra tu favorito.html",contexto)