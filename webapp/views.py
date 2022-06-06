from django.shortcuts import render, HttpResponse
from django.http import HttpResponse    

# Create your views here.

def index (request):
    return render (request, "webapp/index.html")

def estudiantes (request):
    return render(request, 'webapp/estudiantes.html')

def profesores (request):
    return render(request, 'webapp/profesores.html')

