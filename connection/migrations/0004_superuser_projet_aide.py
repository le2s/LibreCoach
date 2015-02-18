# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('connection', '0003_superuser_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='superuser',
            name='projet_aide',
            field=models.ForeignKey(null=True, to='projects.Project', blank=True),
            preserve_default=True,
        ),
    ]
