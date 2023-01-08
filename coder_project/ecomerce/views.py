from ecomerce.models import Productos, Carritos, Cliente
from django.http import HttpResponse
from django.shortcuts import render

# Producto

def crear_producto(request):
    newProd = Productos.objects.create(name="coca", price=200)
    return HttpResponse("Producto creado")
        
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
        Productos.objects.create(name=name, price=price)
        return HttpResponse("Data enviada!")

# Carrito

def crear_carritos(request):
    newCarrito = Carritos.objects.create(name="Carrito de Juan")
    return HttpResponse("Carrito creado")

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
        return HttpResponse("Data enviada!")

# Cliente

def crear_cliente(request):
    newCliente = Cliente.objects.create(name="Mariano", lastName="Lopez")
    return HttpResponse("Cliente creado")


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
        return HttpResponse("Data enviada!")
