# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_auto_20150729_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='auction_end_date',
            field=models.DateTimeField(),
        ),
    ]
