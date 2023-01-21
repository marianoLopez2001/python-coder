"""coder_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecomerce.views import crear_producto, ver_productos, crear_carritos, ver_carritos, crear_cliente, ver_clientes, eliminar_producto

urlpatterns = [
    path('admin/', admin.site.urls),

    path('crearProducto/', crear_producto, name='CrearProducto'),
    path('productos/', ver_productos, name='VerProductos'),
    path('eliminar-producto/<data>', eliminar_producto, name='EliminarProducto'),


    path('crearCarrito/', crear_carritos, name='CrearCarrito'),
    path('carritos/', ver_carritos, name='VerCarritos'),

    path('crearCliente/', crear_cliente, name='CrearCliente'),
    path('clientes/', ver_clientes, name='VerClientes'),
]

