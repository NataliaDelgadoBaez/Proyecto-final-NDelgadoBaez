from django.shortcuts import render
from Tienda_app.models import Disco
from Tienda_app.forms import Discoformulario, BuscaDiscoform



def inicio(request):
    return render(request, "Tienda_app/index.html")

def tienda(request):
    return render(request, "Tienda_app/tienda.html")

def blog(request):
    return render(request, "templates/blog.html")

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


def Discoforms (request):
 
    if request.method == "POST":
 
        miFormulario = Discoformulario(request.POST) 
        print(miFormulario)
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            disco =  Disco(nombre=request.POST['nombre'],autor=request.POST['autor'], año=request.POST['año'])
            disco.save()
            return render(request, "Tienda_app/index.html")
    else:
            miFormulario = Discoformulario()
 
            return render(request, "Tienda_app/Discoformulario.html", {"miFormulario": miFormulario})


def Buscardisco (request):
 
    if request.method == "POST":
 
        miFormulario = Buscardisco(request.POST) 
        print(miFormulario)
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            discos = Disco.objects.filter(nombre_icontains=informacion('disco'))
            
            return render(request, "Tienda_app/buscar disco.html",{"discos": discos})
    else:
            miFormulario = BuscaDiscoform()
 
            return render(request, "Tienda_app/mostrar busqueda.html", {"miFormulario": miFormulario})

