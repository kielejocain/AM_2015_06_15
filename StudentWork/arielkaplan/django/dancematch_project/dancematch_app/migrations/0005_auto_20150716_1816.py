# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dancematch_app', '0004_auto_20150716_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='danceprefs',
            name='competition',
        ),
        migrations.RemoveField(
            model_name='danceprefs',
            name='social',
        ),
        migrations.AddField(
            model_name='danceprefs',
            name='goals',
            field=models.CharField(default=b'Social Dancing', max_length=200, choices=[(b'Social Dance Buddy', b'Social Dance Buddy'), (b'Class Buddy', b'Class Buddy'), (b'Social Dancing', b'Social Dancing'), (b'Competition Routine', b'Competition Routine'), (b'Competition Strictly', b'Competition Strictly'), (b'Other Competition', b'Other Competition')]),
        ),
    ]
