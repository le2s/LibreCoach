# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connection', '0004_superuser_projet_aide'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disponibilite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('jour', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='superuser',
            name='dispo',
            field=models.ForeignKey(blank=True, null=True, to='connection.Disponibilite'),
            preserve_default=True,
        ),
    ]
