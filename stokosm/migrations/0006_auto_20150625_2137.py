# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stokosm', '0005_auto_20150625_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='goal',
            field=models.ForeignKey(related_name='links', blank=True, to='stokosm.Goal', null=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='project',
            field=models.ForeignKey(related_name='links', to='stokosm.Project'),
        ),
        migrations.AlterField(
            model_name='link',
            name='requirement',
            field=models.ForeignKey(related_name='links', blank=True, to='stokosm.Requirement', null=True),
        ),
    ]
