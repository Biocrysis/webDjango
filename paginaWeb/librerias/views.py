from django.shortcuts import render
from django.http import HttpResponse #libreria para realizar peticiones
# Create your views here.

def inici():
    return HttpResponse("<h1> Bienvenido a Django </h1>")
