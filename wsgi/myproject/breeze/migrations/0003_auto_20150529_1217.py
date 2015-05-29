# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('breeze', '0002_tabla_ejemplo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='avatar',
        ),
        migrations.AddField(
            model_name='usuario',
            name='cod_avatar',
            field=models.CharField(default=datetime.datetime(2015, 5, 29, 12, 17, 30, 130422, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
