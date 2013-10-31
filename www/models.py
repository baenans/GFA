# -*- coding: utf-8 -*-
from django.db import models
# Create your models here.
class Planta(models.Model):
	nombreComun = models.CharField(max_length=150)
	nombreCientifico = models.CharField(max_length=150)
	foto= models.ImageField(upload_to="uploads/")
	detalleHoja= models.ImageField(upload_to="uploads/")
	distribucion = models.CharField(max_length=100)
	medida = models.DecimalField(max_digits=6, decimal_places=2)
	tipoDeSuelo = models.CharField(max_length=100)
	altura = models.DecimalField(max_digits=7, decimal_places=2)
	def __unicode__(self):
		return  u"%s (%s)" % (self.nombreCientifico, self.nombreComun)