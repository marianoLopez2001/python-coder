from ecommerce.models import Productos
from django.shortcuts import render, redirect, HttpResponse
from ecommerce.forms import ProductosFormulario 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

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
        formulario = ProductosFormulario()
        context = {"productos": productos, "formulario":formulario}
        return render(request, "productos.html", context=context)
    elif request.method == "GET":
        productos = Productos.objects.all()
        formulario = ProductosFormulario()
        context = {"productos": productos, "formulario":formulario}
        return render(request, "productos.html", context=context)
    elif request.method == "POST":
        formulario = ProductosFormulario(request.POST)
        if formulario.is_valid():
            print('valido')
            info = formulario.cleaned_data
            print(info)
            producto = Productos(name=info['name'], author=info['author'], description=info['description'], image=info['image'], stock=info['stock'], price=info['price'])
            producto.save()
            return redirect("VerProductos")
        else:
            return HttpResponse('no valido')

def eliminar_producto (request, data):
    eliminar = Productos.objects.get(id=data)
    eliminar.delete()
    return redirect('VerProductos')

def detalle_producto (request, data):
    producto = Productos.objects.get(id=data)
    print(producto)
    context={"producto": producto}
    return render(request, 'producto-detalle.html', context = context)

def login_user (request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid(): 
            usuario_nombre = form.cleaned_data.get('username')
            user_password = form.cleaned_data.get('password')
            user = authenticate(username=usuario_nombre, password=user_password)
            if user is not None:
                login(request, user)
                return render(request, 'inicio.html', {"nombre": usuario_nombre, "msg": 'Exito'})
            else: 
                return render(request, 'inicio.html', {"msg": 'Error'})
        else:
            return render(request, 'inicio.html', {"msg": 'Error en form'})

    form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})

def register_user (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'inicio.html', {'msg':f'registrado con exito {username}'})
        else:
            return render(request, 'inicio.html', {'msg':'registrado fallido'})
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form':form})

