from django.db import models

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
		ordering = ['numero_de_Serie']
	
	def __unicode__ (self):
		return "%d | %s" %(self.numero_de_Serie, self.tipo_de_Equipamento)

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
