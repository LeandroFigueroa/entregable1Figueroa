from django.urls import path
from . import views  

urlpatterns = [
    path('', views.index, name='index'),
    path('profesores/', views.profesores, name='profesores'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
]

