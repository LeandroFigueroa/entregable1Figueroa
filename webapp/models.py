from django.db import models
class Estudiantes (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    correo = models.EmailField()
    materia = models.CharField(max_length=50)

class Curso (models.Model):
    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()

class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)