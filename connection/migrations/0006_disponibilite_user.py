# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('connection', '0005_auto_20150217_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='disponibilite',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True),
            preserve_default=True,
        ),
    ]
