# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('direction', models.IntegerField(default=0, choices=[(0, b'Child'), (1, b'Parent')])),
                ('directed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('related', models.ManyToManyField(to='stokosm.Goal', through='stokosm.Connection')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('goal', models.ForeignKey(blank=True, to='stokosm.Goal', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('linked_goals', models.ManyToManyField(related_name='goals', through='stokosm.Link', to='stokosm.Goal')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('related', models.ManyToManyField(to='stokosm.Requirement', through='stokosm.Connection')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='project',
            name='linked_req',
            field=models.ManyToManyField(related_name='requirements', through='stokosm.Link', to='stokosm.Requirement'),
        ),
        migrations.AddField(
            model_name='project',
            name='related',
            field=models.ManyToManyField(to='stokosm.Project', through='stokosm.Connection'),
        ),
        migrations.AddField(
            model_name='link',
            name='project',
            field=models.ForeignKey(to='stokosm.Project'),
        ),
        migrations.AddField(
            model_name='link',
            name='requirement',
            field=models.ForeignKey(blank=True, to='stokosm.Requirement', null=True),
        ),
        migrations.AddField(
            model_name='connection',
            name='goal1',
            field=models.ForeignKey(related_name='connections', blank=True, to='stokosm.Goal', null=True),
        ),
        migrations.AddField(
            model_name='connection',
            name='goal2',
            field=models.ForeignKey(related_name='reverse_connections', blank=True, to='stokosm.Goal', null=True),
        ),
        migrations.AddField(
            model_name='connection',
            name='project1',
            field=models.ForeignKey(related_name='connections', blank=True, to='stokosm.Project', null=True),
        ),
        migrations.AddField(
            model_name='connection',
            name='project2',
            field=models.ForeignKey(related_name='reverse_connections', blank=True, to='stokosm.Project', null=True),
        ),
        migrations.AddField(
            model_name='connection',
            name='requirement1',
            field=models.ForeignKey(related_name='connections', blank=True, to='stokosm.Requirement', null=True),
        ),
        migrations.AddField(
            model_name='connection',
            name='requirement2',
            field=models.ForeignKey(related_name='reverse_connections', blank=True, to='stokosm.Requirement', null=True),
        ),
    ]
