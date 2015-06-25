# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stokosm', '0003_auto_20150622_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='goal1',
            field=models.ForeignKey(related_name='connected', blank=True, to='stokosm.Goal', null=True),
        ),
        migrations.AlterField(
            model_name='connection',
            name='goal2',
            field=models.ForeignKey(related_name='reverse_connected', blank=True, to='stokosm.Goal', null=True),
        ),
        migrations.AlterField(
            model_name='connection',
            name='project1',
            field=models.ForeignKey(related_name='connected', blank=True, to='stokosm.Project', null=True),
        ),
        migrations.AlterField(
            model_name='connection',
            name='project2',
            field=models.ForeignKey(related_name='reverse_connected', blank=True, to='stokosm.Project', null=True),
        ),
        migrations.AlterField(
            model_name='connection',
            name='requirement1',
            field=models.ForeignKey(related_name='connected', blank=True, to='stokosm.Requirement', null=True),
        ),
        migrations.AlterField(
            model_name='connection',
            name='requirement2',
            field=models.ForeignKey(related_name='reverse_connected', blank=True, to='stokosm.Requirement', null=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='related',
            field=models.ManyToManyField(related_name='reverse_related', through='stokosm.Connection', to='stokosm.Node'),
        ),
        migrations.AlterField(
            model_name='project',
            name='linked_goals',
            field=models.ManyToManyField(related_name='linked_projects', through='stokosm.Link', to='stokosm.Goal'),
        ),
        migrations.AlterField(
            model_name='project',
            name='linked_req',
            field=models.ManyToManyField(related_name='linked_projects', through='stokosm.Link', to='stokosm.Requirement'),
        ),
    ]
