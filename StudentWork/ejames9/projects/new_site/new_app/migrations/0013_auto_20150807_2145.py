# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0012_auto_20150807_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofiles',
            name='user',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='user_profile',
        ),
        migrations.DeleteModel(
            name='UserProfiles',
        ),
    ]
