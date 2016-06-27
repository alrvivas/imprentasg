# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_registro', models.DateField(auto_now_add=True, verbose_name=b'Fecha de regidtro')),
                ('nombre', models.CharField(max_length=140, null=True)),
                ('activa', models.BooleanField(default=True)),
                ('rfc', models.CharField(max_length=140, null=True)),
                ('celular', models.CharField(max_length=15, null=True)),
                ('telefono', models.CharField(max_length=15, null=True)),
                ('dias_credito', models.PositiveIntegerField(null=True)),
                ('imagen', models.ImageField(default=b'images/clientes/default-01.jpg', upload_to=b'images/clientes', null=True, verbose_name=b'Imagen Cliente', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_registro', models.DateField(auto_now_add=True, verbose_name=b'Fecha de registro')),
                ('principal', models.BooleanField(default=True)),
                ('nombre', models.CharField(max_length=140, null=True)),
                ('apellidos', models.CharField(max_length=140, null=True)),
                ('celular', models.CharField(max_length=15, null=True)),
                ('telefono', models.CharField(max_length=15, null=True)),
                ('puesto', models.CharField(max_length=140, null=True)),
                ('imagen', models.ImageField(default=b'images/clientes/default-01.jpg', upload_to=b'images/clientes/representantes', null=True, verbose_name=b'Imagen Cliente', blank=True)),
                ('empresa', models.ForeignKey(blank=True, to='clientes.Empresa', null=True)),
            ],
        ),
    ]
