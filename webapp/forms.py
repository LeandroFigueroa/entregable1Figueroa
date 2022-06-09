from django import forms


class ProfesorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

class CursosFormulario(forms.Form):
  curso = forms.CharField(max_length=50)
  camada = forms.IntegerField()

class EstudiantesFormulario(forms.Form):
  nombre = forms.CharField(max_length=50)
  apellido = forms.CharField(max_length=50)
  edad = forms.IntegerField()
  correo = forms.EmailField()
  materia = forms.CharField(max_length=50)