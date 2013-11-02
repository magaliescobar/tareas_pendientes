from django import forms 
from models import Autores, Tareas, Actualizaciones

class AutoresForm(forms.ModelForm):
	class Meta:
		model = Autores

class TareasForm(forms.ModelForm):
	class Meta:
		model = Tareas

class ActualizacionesForm(forms.ModelForm):
	class Meta:
		model = Actualizaciones
 