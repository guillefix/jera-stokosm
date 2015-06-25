# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stokosm', '0002_auto_20150622_0159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published')),
                ('related', models.ManyToManyField(to='stokosm.Node', through='stokosm.Connection')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='goal',
            name='id',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='name',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='related',
        ),
        migrations.RemoveField(
            model_name='project',
            name='id',
        ),
        migrations.RemoveField(
            model_name='project',
            name='name',
        ),
        migrations.RemoveField(
            model_name='project',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='related',
        ),
        migrations.RemoveField(
            model_name='requirement',
            name='id',
        ),
        migrations.RemoveField(
            model_name='requirement',
            name='name',
        ),
        migrations.RemoveField(
            model_name='requirement',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='requirement',
            name='related',
        ),
        migrations.AddField(
            model_name='goal',
            name='node_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='stokosm.Node'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='node_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='stokosm.Node'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requirement',
            name='node_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='stokosm.Node'),
            preserve_default=False,
        ),
    ]
