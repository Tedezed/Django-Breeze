# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.IntegerField(max_length=10)),
                ('text_comentario', models.CharField(max_length=140)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='instrumento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.IntegerField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='partitura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.IntegerField(max_length=10)),
                ('nombre', models.CharField(max_length=70)),
                ('visitas', models.IntegerField(max_length=50)),
                ('archivo_partitura', models.FileField(upload_to=b'.')),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('codigo_instrumento', models.ForeignKey(to='breeze.instrumento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(upload_to=b'images')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='valoracion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.IntegerField(max_length=10)),
                ('tipo', models.IntegerField(max_length=1)),
                ('codigo_partitura', models.ForeignKey(to='breeze.partitura')),
                ('codigo_usuario', models.ForeignKey(to='breeze.usuario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='partitura',
            name='codigo_usuario',
            field=models.ForeignKey(to='breeze.usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comentario',
            name='codigo_partitura',
            field=models.ForeignKey(to='breeze.partitura'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comentario',
            name='codigo_usuario',
            field=models.ForeignKey(to='breeze.usuario'),
            preserve_default=True,
        ),
    ]
