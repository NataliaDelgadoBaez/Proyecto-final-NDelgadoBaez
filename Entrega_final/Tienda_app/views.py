from django.shortcuts import render
from Tienda_app.models import Disco
from Tienda_app.forms import Discoformulario, BuscaDiscoform



def inicio(request):
    return render(request, "Tienda_app/index.html")

def discos(request):
    return render(request, "Tienda_app/discos.html")

def discos_comprados(request):
    return render(request, "Tienda_app/discos comprados.html")

def discos_vendidos(request):
    return render(request, "Tienda_app/discos vendidos.html")

def usuarios(request):
    return render(request, "Tienda_app/usuarios.html")

def iniciar_sesion(request):
    return render(request, "Tienda_app/iniciar sesion.html")

def crear_cuenta(request):
    return render(request, "Tienda_app/crear cuenta.html")


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

