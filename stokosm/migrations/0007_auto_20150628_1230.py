# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stokosm', '0006_auto_20150625_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='connection',
            name='description',
            field=models.CharField(default='Description', max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='link',
            name='description',
            field=models.CharField(default='Description', max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='node',
            name='description',
            field=models.CharField(default='Description', max_length=2000),
            preserve_default=False,
        ),
    ]
