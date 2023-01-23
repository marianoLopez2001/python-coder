from ecommerce.models import Productos
from django.shortcuts import render, redirect, HttpResponse
from ecommerce.forms import ProductosFormulario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import user_passes_test

# Inicio

def inicio(request):
    return render(request, "inicio.html")

# Acerca de mi

def acerca_de_mi(request):
    return render(request, "acerca-de-mi.html")

# Productos

def ver_productos(request):
    if request.method == "GET" and "search" in request.GET:
        search = request.GET["search"]
        productos = Productos.objects.filter(name=search)
        context = {"productos": productos}
        return render(request, "productos.html", context=context)
    elif request.method == "GET":
        productos = Productos.objects.all()
        context = {"productos": productos}
        return render(request, "productos.html", context=context)

def eliminar_producto(request, data):
    eliminar = Productos.objects.get(id=data)
    eliminar.delete()
    return redirect("VerProductos")


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
            return redirect("VerProductos")
        else:
            return HttpResponse("no valido")
