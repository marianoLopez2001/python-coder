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
from ecommerce.views import ver_productos, eliminar_producto, inicio, acerca_de_mi, detalle_producto, login_user, register_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='Inicio'),
    path('acerca-de-mi/', acerca_de_mi, name='AcercaDeMi'),

    path('productos/', ver_productos, name='VerProductos'),
    path('eliminar-producto/<data>', eliminar_producto, name='EliminarProducto'),
    path('detalle-producto/<data>', detalle_producto, name='DetalleProducto'),

    path('login/', login_user, name='Login'),
    path('register/', register_user, name='Register'),
    
]

