from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Hola Mundo! index</h1>")

def texto(request):
    return HttpResponse("<h1>Hola Mundo! esto es un texto app2</h1>")