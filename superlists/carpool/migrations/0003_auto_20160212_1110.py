# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0002_user_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='text',
            new_name='date',
        ),
        migrations.AddField(
            model_name='user',
            name='end',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='nameFirst',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='nameLast',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='start',
            field=models.TextField(default=''),
        ),
    ]
