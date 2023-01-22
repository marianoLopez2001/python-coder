from django import forms
from django.forms import TextInput
from django.contrib.auth.forms import UserCreationForm

class ProductosFormulario (forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Nombre", "class": "form-control"}), max_length=20)
    description = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Descripcion", "class": "form-control"}), max_length=100)
    stock = forms.BooleanField(widget=forms.TextInput(attrs={"placeholder": "Stock", "class": "form-control"}), )
    author = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Autor", "class": "form-control"}), max_length=20)
    date = forms.DateField(widget=forms.TextInput(attrs={"placeholder": "Fecha", "class": "form-control"}), )
    image = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Imagen ('url')", "class": "form-control"}), max_length=200)
    price = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": "Precio", "class": "form-control"}), )

