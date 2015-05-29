# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('breeze', '0003_auto_20150529_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='correo',
            field=models.CharField(default=datetime.datetime(2015, 5, 29, 17, 33, 24, 243143, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
