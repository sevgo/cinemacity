# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Projections',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('projection_type', models.CharField(max_length=3)),
                ('projection_date', models.DateField()),
                ('projection_time', models.TimeField()),
                ('movie_id', models.ForeignKey(to='website.Movies')),
            ],
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('username', models.CharField(max_length=64)),
                ('row', models.PositiveSmallIntegerField()),
                ('col', models.PositiveSmallIntegerField()),
                ('projection_id', models.ForeignKey(to='website.Projections')),
            ],
        ),
    ]
