# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dancematch_app', '0003_auto_20150715_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='danceprefs',
            name='follow_level',
            field=models.CharField(default=b'New', max_length=200, choices=[(b'New', b'Brand New'), (b'Beginner', b'Beginner'), (b'Beyond Beginning', b'Beyond Beginning'), (b'Intermediate', b'Intermediate'), (b'Advanced', b'Advanced'), (b'Expert', b'Expert')]),
        ),
        migrations.AddField(
            model_name='danceprefs',
            name='lead_level',
            field=models.CharField(default=b'New', max_length=200, choices=[(b'New', b'Brand New'), (b'Beginner', b'Beginner'), (b'Beyond Beginning', b'Beyond Beginning'), (b'Intermediate', b'Intermediate'), (b'Advanced', b'Advanced'), (b'Expert', b'Expert')]),
        ),
    ]
