# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='character_name',
            field=models.CharField(default=b'Stop Having a German Name!', max_length=50),
        ),
    ]
