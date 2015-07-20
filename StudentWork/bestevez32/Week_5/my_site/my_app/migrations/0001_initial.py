# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agility_score', models.IntegerField()),
                ('smarts_score', models.IntegerField()),
                ('strength_score', models.IntegerField()),
                ('spirit_score', models.IntegerField()),
                ('vigor_score', models.IntegerField()),
            ],
        ),
    ]
