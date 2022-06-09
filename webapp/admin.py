from django.contrib import admin
from .models import Profesor, Estudiantes, Curso

# Register your models here.

admin.site.register(Curso)
admin.site.register(Estudiantes)
admin.site.register(Profesor)


