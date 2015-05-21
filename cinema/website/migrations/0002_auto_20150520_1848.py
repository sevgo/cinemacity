# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projection',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('type', models.SmallIntegerField(default=1, choices=[(1, '2D'), (2, '3D'), (3, '4DX')])),
                ('time', models.DateTimeField()),
                ('hall', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('row', models.PositiveSmallIntegerField()),
                ('col', models.PositiveSmallIntegerField()),
                ('projection', models.ForeignKey(to='website.Projection')),
            ],
        ),
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
        migrations.RemoveField(
            model_name='projections',
            name='movie_id',
        ),
        migrations.RemoveField(
            model_name='reservations',
            name='projection_id',
        ),
        migrations.DeleteModel(
            name='Projections',
        ),
        migrations.DeleteModel(
            name='Reservations',
        ),
        migrations.AddField(
            model_name='projection',
            name='movie',
            field=models.ForeignKey(to='website.Movie'),
        ),
    ]
