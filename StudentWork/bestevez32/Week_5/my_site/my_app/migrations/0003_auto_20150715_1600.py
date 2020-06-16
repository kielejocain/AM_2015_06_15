# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_character_character_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='character_name',
            field=models.CharField(default=b'Enter next name here', max_length=50),
        ),
    ]
