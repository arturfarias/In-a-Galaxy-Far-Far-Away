# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=200)),
                ('sexo', models.CharField(max_length=1, choices=[(b'F', b'Feminino'), (b'M', b'Masculino')])),
                ('datanascimento', models.DateField(null=True, verbose_name='Data de Nascimento', blank=True)),
                ('email', models.EmailField(max_length=200)),
                ('telefone', models.CharField(max_length=9)),
                ('senha', models.CharField(max_length=30)),
                ('endereco', models.CharField(max_length=200, null=True, verbose_name='Endere\xe7o', blank=True)),
                ('numero', models.CharField(max_length=200, null=True, verbose_name='N\xfamero', blank=True)),
                ('complemento', models.CharField(max_length=200, null=True, blank=True)),
                ('cep', models.CharField(max_length=9)),
                ('bairro', models.CharField(max_length=200, null=True, blank=True)),
                ('estado', models.CharField(max_length=2)),
                ('cidade', models.CharField(max_length=200)),
                ('datacadastro', models.DateTimeField(auto_now_add=True)),
                ('foto', models.ImageField(null=True, upload_to=b'cadastros/%Y', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
