# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stokosm', '0004_auto_20150624_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='goal1',
            field=models.ForeignKey(related_name='connections', blank=True, to='stokosm.Goal', null=True),
        ),
        migrations.AlterField(
            model_name='connection',
            name='goal2',
            field=models.ForeignKey(related_name='reverse_connections', blank=True, to='stokosm.Goal', null=True),
        ),
        migrations.AlterField(
            model_name='connection',
            name='project1',
            field=models.ForeignKey(related_name='connections', blank=True, to='stokosm.Project', null=True),
        ),
        migrations.AlterField(
            model_name='connection',
            name='project2',
            field=models.ForeignKey(related_name='reverse_connections', blank=True, to='stokosm.Project', null=True),
        ),
        migrations.AlterField(
            model_name='connection',
            name='requirement1',
            field=models.ForeignKey(related_name='connections', blank=True, to='stokosm.Requirement', null=True),
        ),
        migrations.AlterField(
            model_name='connection',
            name='requirement2',
            field=models.ForeignKey(related_name='reverse_connections', blank=True, to='stokosm.Requirement', null=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='goal',
            field=models.ForeignKey(related_name='goal_links', blank=True, to='stokosm.Goal', null=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='requirement',
            field=models.ForeignKey(related_name='requirement_links', blank=True, to='stokosm.Requirement', null=True),
        ),
    ]
