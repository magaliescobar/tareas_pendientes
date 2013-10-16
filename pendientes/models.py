from django.db import models

# Create your models here.


estado_tareas = (
	("no_iniciada" , "No iniciada"),
	("en_proceso" , "En proceso"),
	("suspendida" , "Suspendida"),
	("finalizada" , "Finalizada"),
)

class Autores(models.Model):
	nombre = models.CharField(max_length=30)

	def __unicode__(self):
		return "%s" %(self.nombre)

	class Meta():
		verbose_name_plural="Autores"



class Tareas(models.Model):
	titulo = models.CharField(max_length=30)
	fecha_creacion = models.DateField()
	alcance = models.CharField(max_length=30)
	autor = models.ForeignKey(Autores)
	estado = models.CharField(max_length=11, choices=estado_tareas)

	def __unicode__(self):
		return "%s - %s - %s - %s" %(self.titulo, self.fecha_creacion,self.alcance,self.autor)

	class Meta():
		verbose_name_plural = "Tareas"






