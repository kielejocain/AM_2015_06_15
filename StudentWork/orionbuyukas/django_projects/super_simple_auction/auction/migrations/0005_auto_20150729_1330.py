# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_auto_20150729_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='auction_end_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
