# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class TipoSuelo(models.Model):
	nombre = models.CharField(max_length=100)
	def __unicode__(self):
		return u"%s" % (self.nombre)
class Planta(models.Model):
	nombreCientifico = models.CharField(max_length=150)
	nombreComun = models.CharField(max_length=150)
	foto = models.ImageField(upload_to="gfa/")
	detalleHoja = models.ImageField(upload_to="gfa/")
	distribucion = models.CharField(max_length=100)
	longitud = models.CharField(max_length=50)
	tipoDeSuelo = models.ForeignKey(TipoSuelo)
	altitud = models.CharField(max_length=50)
	creador = models.ForeignKey(User)
	def __unicode__(self):
		return  u"%s (%s)" % (self.nombreCientifico, self.nombreComun)