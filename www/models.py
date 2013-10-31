
from django.db import models

# Create your models here.
class Planta(models.Model):
	nombreComun = models.CharField(max_lenght=150)
	nombreCientifico = models.CharField(max_lenght=150)