# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dancematch_app', '0006_danceprefs_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='danceprefs',
            name='notes',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
