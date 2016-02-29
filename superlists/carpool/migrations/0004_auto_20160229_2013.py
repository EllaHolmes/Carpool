# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0003_auto_20160212_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nameFirst', models.TextField(default='')),
                ('nameLast', models.TextField(default='')),
                ('start', models.TextField(default='')),
                ('end', models.TextField(default='')),
                ('date', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nameFirst', models.TextField(default='')),
                ('nameLast', models.TextField(default='')),
                ('start', models.TextField(default='')),
                ('end', models.TextField(default='')),
                ('date', models.TextField(default='')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
