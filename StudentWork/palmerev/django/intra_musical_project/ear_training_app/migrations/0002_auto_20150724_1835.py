# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ear_training_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='chord_answer',
            field=models.ForeignKey(blank=True, to='ear_training_app.Chord', null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='interval_answer',
            field=models.ForeignKey(blank=True, to='ear_training_app.Interval', null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='scale_answer',
            field=models.ForeignKey(blank=True, to='ear_training_app.Scale', null=True),
        ),
        migrations.AlterField(
            model_name='exercisepage',
            name='exercise',
            field=models.ForeignKey(blank=True, to='ear_training_app.Exercise', null=True),
        ),
    ]
