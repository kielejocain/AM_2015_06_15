# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djmmdemo_app', '0002_auto_20150831_2031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='performer',
            new_name='owner',
        ),
    ]
