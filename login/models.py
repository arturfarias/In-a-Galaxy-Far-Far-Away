# coding: utf-8
from django.db import models

SEXO_C = (('F','Feminino'),('M','Masculino'),)

class Cadastro (models.Model):
    user = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=200)
    sexo = models.CharField(max_length=1,choices=SEXO_C)
    datanascimento = models.DateField(verbose_name=u'Data de Nascimento', null=True, blank=True)
    email = models.EmailField(max_length=200)
    telefone = models.CharField(max_length=9)
    senha = models.CharField(max_length=30)
    endereco = models.CharField(max_length=200, verbose_name=u'Endereço', blank=True, null=True)
    numero = models.CharField(max_length=200, verbose_name=u'Número', blank=True, null=True)
    complemento = models.CharField(max_length=200, blank=True, null=True)
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=200, blank=True, null=True)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=200)
    datacadastro = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to='cadastros/%Y',null=True,blank=True)
