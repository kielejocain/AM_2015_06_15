# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_auto_20150728_1618'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bid',
            options={'ordering': ['bid_amount']},
        ),
        migrations.AddField(
            model_name='auction',
            name='price',
            field=models.DecimalField(default=0.0, max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='auction',
            name='auction_end_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 29, 13, 21, 6, 134000)),
        ),
    ]
