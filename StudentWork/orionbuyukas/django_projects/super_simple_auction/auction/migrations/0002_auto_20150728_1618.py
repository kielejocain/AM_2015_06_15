# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='opening_bid',
        ),
        migrations.AddField(
            model_name='auction',
            name='item',
            field=models.ForeignKey(default=datetime.datetime(2015, 7, 28, 23, 17, 59, 803000, tzinfo=utc), to='auction.Item'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bid',
            name='auction',
            field=models.ForeignKey(default=datetime.datetime(2015, 7, 28, 23, 18, 18, 436000, tzinfo=utc), to='auction.Auction'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='auction',
            name='opening_bid',
            field=models.DecimalField(default=1.0, max_digits=7, decimal_places=2),
        ),
    ]
