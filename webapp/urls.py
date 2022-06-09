from django.urls import path, include
from . import views       



urlpatterns = [
    path('', views.index, name='index'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    #path('cursos/', views.cursos, name='cursos'),
    path('profesores', views.profesores, name="profesores"),
    path('estudiantes', views.estudiantes, name="estudiantes"),
    path('cursosFormulario', views.cursosFormulario, name="cursosFormulario"),
    path('busquedaCamada', views.busquedaCamada, name="busquedaCamada"), 
    path('buscar/', views.buscar, name="buscar"),
]


