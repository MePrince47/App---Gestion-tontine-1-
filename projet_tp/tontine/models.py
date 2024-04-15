from django.db import models

# Create your models here.

class La_tontine(models.Model):
	nom = models.CharField(max_length=70)
	slogan = models.CharField(max_length=170)
	regle = models.CharField(max_length=70)

class Le_membre(models.Model):
	nom = models.CharField(max_length=70)
	Prénom = models.CharField(max_length=170)
	Email = models.CharField(max_length=70)
	tontine = models.CharField(max_length=70)
	Nombre_parts = models.CharField(max_length=70)
	statut = models.CharField(max_length=70)
