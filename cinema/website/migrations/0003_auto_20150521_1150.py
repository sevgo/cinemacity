# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20150520_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='projection',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 5, 21, 11, 50, 25, 597578, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projection',
            name='time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='projection',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, '2D'), (2, '3D'), (3, '4DX')], default=1),
        ),
    ]
