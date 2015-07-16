# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dancematch_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DancePrefs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lead', models.BooleanField()),
                ('follow', models.BooleanField()),
                ('competition', models.BooleanField()),
                ('social', models.BooleanField()),
                ('dancer', models.ForeignKey(to='dancematch_app.Dancer')),
            ],
        ),
        migrations.AddField(
            model_name='dance',
            name='description',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='dance',
            name='name',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
