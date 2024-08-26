from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display(request):
    return HttpResponse("<h1>Hola Mundo!</h1>")


def vista1 (request):
    return  HttpResponse("<h1>Hola Mundo!2</h1>")