from django.shortcuts import render
from Tienda_app.models import Disco, Producto, Carrito
from Tienda_app.forms import Crearalbumform, Buscaralbumform, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect




def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid(): 

            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')

            nombre_usuario = authenticate(username= usuario, password=clave)

            if usuario is not None:
                login (request, nombre_usuario)
                return render(request, "Tienda_app/tienda.html", {"mensaje":f"Has iniciado sesion, Bienvenido {usuario}"})
            else:
                return render(request, "Tienda_app/login.html", {"mensaje":"Usuario o contraseña incorrecta"})
           
        else:

            return render(request,"Tienda_app/login.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "Tienda_app/login.html", {"form": form})

def register(request):

      if request.method == 'POST':

            
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"Tienda_app/register.html")

      else:
                 
            form = UserRegisterForm()     

      return render(request,"Tienda_app/soy nuevo.html" ,  {"form":form})

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

def final_carrito(request):
    return render(request, "Tienda_app/fcarrito.html")

def agregar_al_carrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    carrito.productos.add(producto)
    return redirect('carrito')

def destacados(request):
    return render(request, "Tienda_app/destacados.html")

def iniciar_sesion(request):
    return render(request, "Tienda_app/login.html")

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