# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stokosm', '0008_auto_20150628_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='connection',
            name='ranking',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='link',
            name='ranking',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='node',
            name='ranking',
            field=models.IntegerField(default=0),
        ),
    ]
