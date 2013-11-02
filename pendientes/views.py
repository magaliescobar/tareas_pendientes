from django.shortcuts import render
from forms import AutoresForm, TareasForm, ActualizacionesForm

def nuevoAutor(request):
	if request.method == "POST":
		form = AutoresForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Nuevo autor creado")
	else:
		form = AutoresForm()
	return render(request,"Autores/nuevoAutor.html",{
		"form" : form
		})

def eliminarAutor(request,id):
	pass

def editarAutor(request,id):
	pass

def listarAutores(request):
	pass

def nuevaTarea(request):
	pass

def eliminarTarea(request, id):
	pass

def editarTarea(request, id):
	pass

def listarTareas(request):
	pass

def nuevaActualizacion(request):
	pass

def eliminarActualizacion(request, id):
	pass

def editarActualizacion(request, id):
	pass

def listarActualizaciones(request):
	pass





 	
