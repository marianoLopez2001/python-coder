from ecommerce.models import Productos, Community
from django.shortcuts import render, redirect, HttpResponse
from ecommerce.forms import ProductosFormulario, CommunityFormulario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.edit import UpdateView

class ProductoUpdate (UpdateView):

    model = Productos
    success_url = '/posts'
    fields = ['name', 'price']

# Inicio

def inicio(request):
    return render(request, "inicio.html")

# Acerca de mi

def acerca_de_mi(request):
    return render(request, "acerca-de-mi.html")

# Productos

def ver_posts(request):
    if request.method == "GET" and "search" in request.GET:
        search = request.GET["search"]
        productos = Productos.objects.filter(name=search)
        context = {"productos": productos}
        return render(request, "posts.html", context=context)
    elif request.method == "GET":
        productos = Productos.objects.all()
        comunidades = Community.objects.all()
        context = {"productos": productos, 'comunidades': comunidades}
        return render(request, "posts.html", context=context)

def eliminar_producto(request, data):
    eliminar = Productos.objects.get(id=data)
    eliminar.delete()
    return redirect("VerPosts")


def actualizar_producto(request, data):
    productoUpdate = Productos.objects.filter(id=data)
    print(productoUpdate)
    if request.method == "POST":
        form = ProductosFormulario(request.POST)
        if form.is_valid():
            username = form.cleaned_data["name"]
            author = form.cleaned_data["author"]
            description = form.cleaned_data["description"]
            image = form.cleaned_data["image"]
            stock = form.cleaned_data["stock"]
            price = form.cleaned_data["price"]
            productoUpdate.update(name=username, author=author, description= description, image=image, stock=stock, price=price)
            return redirect("/posts")
        else:
            return render(request, "formulario-productos.html", {"formulario":form})
    else:
        form = ProductosFormulario()
        return render(request, "formulario-productos.html", {"formulario":form})




def detalle_producto(request, data):
    producto = Productos.objects.get(id=data)
    context = {"producto": producto}
    return render(request, "producto-detalle.html", context=context)


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario_nombre = form.cleaned_data.get("username")
            user_password = form.cleaned_data.get("password")
            user = authenticate(username=usuario_nombre, password=user_password)
            if user is not None:
                login(request, user)
                return render(
                    request, "inicio.html", {"nombre": usuario_nombre}
                )
            else:
                return render(request, "inicio.html")
        else:
            return render(request, "inicio.html")

    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(
                request, "inicio.html", {"msg": f"registrado con exito {username}"}
            )
        else:
            return render(request, "inicio.html")
    else:
        form = UserCreationForm()
        return render(request, "register.html", {"form": form})


@user_passes_test(lambda u: u.is_superuser)
def form_products(request):
    if request.method == "GET":
        formulario = ProductosFormulario()
        context = {"formulario": formulario}
        return render(request, "formulario-productos.html", context=context)
    elif request.method == "POST":
        formulario = ProductosFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            producto = Productos(
                name=info["name"],
                author=info["author"],
                description=info["description"],
                image=info["image"],
                stock=info["stock"],
                price=info["price"],
            )
            producto.save()
            return redirect("VerPosts")
        else:
            return HttpResponse("no valido")

# COMUNIDADES

@user_passes_test(lambda u: u.is_superuser)
def form_community(request):
    if request.method == "GET":
        formulario = CommunityFormulario()
        context = {"formulario": formulario}
        return render(request, "formulario-community.html", context=context)
    elif request.method == "POST":
        formulario = CommunityFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            comunidad = Community(
                name=info["name"],
                author=info["author"],
                description=info["description"],
                image=info["image"],
            )
            comunidad.save()
            return redirect("VerPosts")
        else:
            return HttpResponse("no valido")

def eliminar_comunidad(request, data):
    eliminar = Community.objects.get(id=data)
    eliminar.delete()
    return redirect("VerPosts")