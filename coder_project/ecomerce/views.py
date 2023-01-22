from ecomerce.models import Productos, Carritos, Cliente
from django.http import HttpResponse
from django.shortcuts import render, redirect   

#Inicio

def inicio (request):
    return render(request, 'inicio.html')

#Acerca de mi

def acerca_de_mi (request):
    return render(request, 'acerca-de-mi.html')

# Producto
        
def ver_productos(request):
    if request.method == "GET" and 'search' in request.GET:
        search = request.GET['search']
        productos = Productos.objects.filter(name=search)
        context={"productos": productos}
        return render(request, "productos.html", context=context)
    elif request.method == "GET":
        productos = Productos.objects.all()
        context = {"productos": productos}
        return render(request, "productos.html", context=context)
    elif request.method == "POST":
        name = request.POST["name"]
        price = request.POST["price"]
        description = request.POST["description"]
        image = request.POST["image"]
        Productos.objects.create(name=name, price=price, description=description, image=image)
        return redirect("VerProductos")

def eliminar_producto (request, data):
    eliminar = Productos.objects.get(id=data)
    eliminar.delete()
    return redirect('VerProductos')

def detalle_producto (request, data):
    producto = Productos.objects.get(id=data)
    print(producto)
    context={"producto": producto}
    return render(request, 'producto-detalle.html', context = context)

# Carrito

def ver_carritos(request):
    if request.method == "GET" and 'search' in request.GET:
        search = request.GET['search']
        carritos = Carritos.objects.filter(name=search)
        context={"carritos": carritos}
        return render(request, "carritos.html", context=context)
    elif request.method == "GET":
        carritos = Carritos.objects.all()
        context = {"carritos": carritos}
        return render(request, "carritos.html", context=context)
    elif request.method == "POST":
        name = request.POST["name"]
        Carritos.objects.create(name=name)
        return redirect("VerCarritos")

def eliminar_carrito (request, data):
    eliminar = Carritos.objects.get(id=data)
    eliminar.delete()
    return redirect('VerCarritos')

# Cliente

def ver_clientes(request):
    if request.method == "GET" and 'search' in request.GET:
        search = request.GET['search']
        clientes = Cliente.objects.filter(name=search)
        context={"clientes": clientes}
        return render(request, "clientes.html", context=context)
    elif request.method == "GET":
        clientes = Cliente.objects.all()
        context = {"clientes": clientes}
        return render(request, "clientes.html", context=context)
    elif request.method == "POST":
        name = request.POST["name"]
        lastName = request.POST["lastName"]
        Cliente.objects.create(name=name, lastName=lastName)
        return redirect("VerClientes")

def eliminar_cliente (request, data):
    eliminar = Cliente.objects.get(id=data)
    eliminar.delete()
    return redirect('VerClientes')

