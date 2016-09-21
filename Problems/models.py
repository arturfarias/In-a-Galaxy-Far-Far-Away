from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver

class Lab(models.Model):

	laboratorio_cad = models.CharField(unique=True,max_length=6)

	def __unicode__ (self):
			return self.laboratorio_cad

class Tipo_de_equipamento(models.Model):
	tipo = models.CharField(unique=True,max_length=30)

	def __unicode__ (self):
			return self.tipo
class Equipamento(models.Model):

	laboratorio = models.ForeignKey(Lab)
	numero_de_Serie = models.CharField(unique=True,max_length=10)
	tipo_de_Equipamento = models.ForeignKey(Tipo_de_equipamento)

	class Meta:
		ordering = ['laboratorio', 'numero_de_Serie']

	def __unicode__ (self):
		return "%s | %s | %8s" %(self.numero_de_Serie, self.tipo_de_Equipamento, self.laboratorio)

class Problema(models.Model):

	problema_Resolvido = models.BooleanField(default=False)
	equipamento = models.ForeignKey(Equipamento)
	descricao = models.TextField()

	class Meta:
		ordering = ['problema_Resolvido']

	def __unicode__ (self):

		if self.problema_Resolvido:
			return "RESOLVIDO"
		else:
			return "EM ANDAMENTO %s" %(self.equipamento)
