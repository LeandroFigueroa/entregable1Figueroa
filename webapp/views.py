
from django import views
from django.shortcuts import render, HttpResponse
from django.template import loader
from django.http import HttpResponse    
from webapp.forms import ProfesorFormulario, CursosFormulario, EstudiantesFormulario
from webapp.models import  Profesor,Curso,Estudiantes

def index   (request):
  return render(request, 'webapp/index.html')

def estudiantes(request):
    if request.method == 'POST':
        miFormulario = EstudiantesFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data   
            estudiante = Estudiantes(nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'], correo=informacion['correo'], materia=informacion['materia'])
            estudiante.save()
            return render(request, 'webapp/index.html')
    
    else:
            miFormulario = EstudiantesFormulario() #Creo mi formulario vacío
    return render(request, 'webapp/estudiantes.html', {'miFormulario':miFormulario})


def profesores(request):

      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid():   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], profesion=informacion['profesion']) 

                  profesor.save()

                  return render(request, "webapp/index.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ProfesorFormulario() #Formulario vacio para construir el html

      return render(request, "webapp/profesores.html", {"miFormulario":miFormulario})


def cursosFormulario(request):
    if request.method == 'POST':
        miFormulario = CursosFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data   
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()

            return render(request, 'webapp/index.html')
    
    else:
            miFormulario = CursosFormulario() #Creo mi formulario vacío
    return render(request, 'webapp/cursosFormulario.html', {'miFormulario':miFormulario})

def busquedaCamada(request):
  return render(request, 'webapp/busquedaCamada.html')

def buscar(request):
    if request.GET['camada']:
     camada = request.GET['camada']
     cursos = Curso.objects.filter(camada=camada)
     return render(request, 'webapp/resultadosBusqueda.html', {'cursos':cursos, 'camada':camada})
    else:
     respuesta = "No se ingresó ninguna camada"
    return HttpResponse(respuesta) 