# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('laboratorio', models.CharField(max_length=20, choices=[(b'LECC1', b'LECC1'), (b'LECC2', b'LECC2')])),
                ('numero_de_Serie', models.IntegerField(unique=True)),
                ('tipo_de_Equipamento', models.CharField(max_length=20, choices=[('gabinete', b'Gabinete'), ('estabilizador', b'Estabilizador'), ('impressora', b'Impressora')])),
            ],
            options={
                'ordering': ['numero_de_Serie'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Problema',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('problema_Resolvido', models.BooleanField(default=False)),
                ('descricao', models.TextField()),
                ('equipamento', models.ForeignKey(to='Problems.Equipamento')),
            ],
            options={
                'ordering': ['problema_Resolvido'],
            },
            bases=(models.Model,),
        ),
    ]
