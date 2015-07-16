# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dancematch_app', '0002_auto_20150715_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='dance',
            name='dance_community',
            field=models.ManyToManyField(to='dancematch_app.Dancer', through='dancematch_app.DancePrefs'),
        ),
        migrations.AddField(
            model_name='danceprefs',
            name='dance',
            field=models.ForeignKey(default='', to='dancematch_app.Dance'),
            preserve_default=False,
        ),
    ]
