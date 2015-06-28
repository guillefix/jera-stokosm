# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stokosm', '0007_auto_20150628_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='description',
            field=models.CharField(max_length=2000, blank=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='description',
            field=models.CharField(max_length=2000, blank=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='description',
            field=models.CharField(max_length=2000, blank=True),
        ),
    ]
