from familiares.models import Familiares
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def familiares_view(request):
    newFamiliar = Familiares.objects.create(name="emaniel", age=12, is_male=True)
    return HttpResponse('Familiar agregado')

def familiares(request):
    familiares = Familiares.objects.all()
    context = {'familiares': familiares}
    return render(request, 'ver_familiares.html', context=context)
