from django import forms


class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=64)
    comision = forms.IntegerField(required=True, max_value=2000)


class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=256)
    apellido = forms.CharField(max_length=256)
    profesion = forms.CharField(max_length=128)


class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=256)
    apellido = forms.CharField(max_length=256)
    email = forms.CharField(max_length=128)
   