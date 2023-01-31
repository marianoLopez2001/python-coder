from django import forms
from django.forms import TextInput
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User

class ProductosFormulario (forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Nombre", "class": "form-control"}), max_length=20)
    description = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Descripcion", "class": "form-control"}), max_length=100)
    stock = forms.BooleanField(widget=forms.TextInput(attrs={"placeholder": "Stock", "class": "form-control"}), )
    author = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Autor", "class": "form-control"}), max_length=20)
    date = forms.DateField(widget=forms.TextInput(attrs={"placeholder": "Fecha", "class": "form-control"}), )
    image = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Imagen ('url')", "class": "form-control"}), max_length=200)
    price = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": "Precio", "class": "form-control"}), )

class CommunityFormulario (forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Nombre", "class": "form-control"}), max_length=20)
    description = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Descripcion", "class": "form-control"}), max_length=100)
    author = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Autor", "class": "form-control"}), max_length=20)
    image = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Imagen ('url')", "class": "form-control"}), max_length=200)

class UserEditForm (UserCreationForm):
    email = forms.EmailField()
    last_name = forms.CharField()
    first_name = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name']
    