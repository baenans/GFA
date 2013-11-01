# -*- coding: utf-8 -*-
from django.db import models
# Create your models here.

class TipoSuelo(models.Model):
	nombre = models.CharField(max_length=100)
	def __unicode__(self):
		return u"%s" % (self.nombre)
class Planta(models.Model):
	nombreComun = models.CharField(max_length=150)
	nombreCientifico = models.CharField(max_length=150)
	distribucion = models.CharField(max_length=100)
	longitud = models.DecimalField(max_digits=6, decimal_places=2)
	tipoDeSuelo = models.ForeignKey(TipoSuelo)
	altitud = models.CharField(max_length=50)
	def __unicode__(self):
		return  u"%s (%s)" % (self.nombreCientifico, self.nombreComun)