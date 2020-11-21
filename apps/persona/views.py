from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Persona



# Create your views here

def ListaPersonasView(request):
    personas = Persona.objects.all()
    return render (request, 'listaPersonas.html',{'personas':personas})
