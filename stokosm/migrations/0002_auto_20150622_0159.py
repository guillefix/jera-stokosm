# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stokosm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='link',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published'),
        ),
    ]
