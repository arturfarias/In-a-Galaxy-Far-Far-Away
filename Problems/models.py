from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver

class Equipamento(models.Model):

	laboratorio = models.CharField(
		choices=(
			('LECC1', 'LECC1'),
			('LECC2', 'LECC2'),
		), max_length = 20
	)

	numero_de_Serie = models.IntegerField(unique=True)
	tipo_de_Equipamento = models.CharField(
		choices=(
			(u'gabinete', "Gabinete"),
			(u'estabilizador', "Estabilizador"),
			(u'impressora', "Impressora"),
		), max_length = 20
	)
	class Meta:
		ordering = ['laboratorio', 'numero_de_Serie']

	def __unicode__ (self):
		return "%d | %s | %8s" %(self.numero_de_Serie, self.tipo_de_Equipamento, self.laboratorio)

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

@receiver(pre_save, sender=Problema)
def handler_limitar_problema(sender, instance, **kwargs):
	equipamento = instance.equipamento

	if not instance.problema_Resolvido:
		retorno = equipamento.problema_set.filter(problema_Resolvido=False)

		if retorno:
			raise ValidationError("Erro interno")
