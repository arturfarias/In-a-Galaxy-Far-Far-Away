# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#======= Banco de dados onde esta armasenada as informacoes do perfil ==========

class Perfil(models.Model):
    user = models.OneToOneField(User)

    SEXO_C = (('N','Não Especificado'),('F','Feminino'),('M','Masculino'),)

    nome = models.CharField(max_length=50,default="")
    sobrenome = models.CharField(max_length=200,default="")
    sexo = models.CharField(max_length=1,choices=SEXO_C,default="N")
    datanascimento = models.CharField(verbose_name=u'Data de Nascimento',max_length=200,default="")
    email = models.EmailField(max_length=200,default="")
    telefone = models.CharField(max_length=9,default="")
    senha = models.CharField(max_length=30,default="")
    endereco = models.CharField(max_length=200, verbose_name=u'Endereço',default="")
    numero = models.CharField(max_length=200, verbose_name=u'Número',default="")
    complemento = models.CharField(max_length=200,default="")
    cep = models.CharField(max_length=9,default="")
    bairro = models.CharField(max_length=200,default="")
    estado = models.CharField(max_length=2,default="")
    cidade = models.CharField(max_length=200,default="")
    datacadastro = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to='Perfil_img/%Y',default="")

    def __unicode__(self): #Usando apenas para indentificacao dos dados no admin do django
        return self.nome

#======== Usado para criar e  vincular o usuario criado ao seu perfil ==========

def cria_user_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

post_save.connect(cria_user_perfil, sender=User)
