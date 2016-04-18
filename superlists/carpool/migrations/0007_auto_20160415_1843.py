# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0006_latlng_route'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='route_string',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='rider',
            name='route_string',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='route',
            name='end_pos',
            field=models.OneToOneField(related_name='end_pos', default=None, to='carpool.LatLng'),
        ),
        migrations.AddField(
            model_name='route',
            name='start_pos',
            field=models.OneToOneField(related_name='start_pos', default=None, to='carpool.LatLng'),
        ),
        migrations.AlterField(
            model_name='latlng',
            name='lat',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='latlng',
            name='lng',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
