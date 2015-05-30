# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('breeze', '0004_usuario_correo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='correo',
        ),
        migrations.AddField(
            model_name='usuario',
            name='docfile',
            field=models.FileField(default=datetime.datetime(2015, 5, 30, 13, 1, 4, 645969, tzinfo=utc), upload_to=b'img_avatar'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='filename',
            field=models.CharField(default=datetime.datetime(2015, 5, 30, 13, 1, 14, 965959, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
