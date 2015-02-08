# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superuser',
            name='phone',
            field=models.CharField(blank=True, max_length=10),
            preserve_default=True,
        ),
    ]
