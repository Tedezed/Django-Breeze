# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('breeze', '0005_auto_20150530_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='cod_avatar',
        ),
    ]
