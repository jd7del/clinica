from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Usuario(models.Model):
	"""docstring for Animal"""
	cedula = models.IntegerField(primary_key=True)
	nombres = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	passowrd = models.CharField(max_length=300)

	def __str__(self):
		return '{}'.format(self.nombres)

class Profesional(models.Model):
	cedula = models.IntegerField(primary_key=True)
	nombres = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	especialidad = models.CharField(max_length=50)
	fecha_vinculacion = models.DateField()

	def __str__(self):
		return '{}'.format(self.nombres)

class Cita_medica(models.Model):
	
	fecha_programada = models.DateField()
	hora_programada = models.DateField()
	fecha_atendida = models.DateField(null=True,blank=True)
	observacion = models.CharField(null=True,blank=True,max_length=200)
	estado = models.BooleanField(default=True)
	profesional = models.ForeignKey(Profesional, null=True,blank=True, on_delete=models.CASCADE)
	usuario = models.ForeignKey(Usuario, null=True,blank=True, on_delete=models.CASCADE)