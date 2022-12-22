from django.http import HttpResponse
from django.shortcuts import render

def home_view (request):
    context = {'saludo': 'Bienvenido...'}
    return render(request, 'home.html', context=context)