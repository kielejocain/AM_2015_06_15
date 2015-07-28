# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChordType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quality', models.CharField(max_length=20, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseContents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseProgress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseSelection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('chord_answer', models.ForeignKey(to='ear_training_app.Chord', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExercisePage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exercise', models.ForeignKey(to='ear_training_app.Exercise', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Interval',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='IntervalType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quality', models.CharField(max_length=20, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=3, blank=True)),
                ('octave', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Scale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('ascending', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScaleType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quality', models.CharField(max_length=25, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='scale',
            name='quality',
            field=models.ForeignKey(to='ear_training_app.ScaleType', null=True),
        ),
        migrations.AddField(
            model_name='scale',
            name='tonic',
            field=models.ForeignKey(to='ear_training_app.Note', null=True),
        ),
        migrations.AddField(
            model_name='interval',
            name='bottom_note',
            field=models.ForeignKey(related_name='bottom_note', blank=True, to='ear_training_app.Note', null=True),
        ),
        migrations.AddField(
            model_name='interval',
            name='name',
            field=models.ForeignKey(blank=True, to='ear_training_app.IntervalType', null=True),
        ),
        migrations.AddField(
            model_name='interval',
            name='top_note',
            field=models.ForeignKey(related_name='top_note', blank=True, to='ear_training_app.Note', null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='interval_answer',
            field=models.ForeignKey(to='ear_training_app.Interval', null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='scale_answer',
            field=models.ForeignKey(to='ear_training_app.Scale', null=True),
        ),
        migrations.AddField(
            model_name='chord',
            name='quality',
            field=models.ForeignKey(to='ear_training_app.ChordType', null=True),
        ),
        migrations.AddField(
            model_name='chord',
            name='root',
            field=models.ForeignKey(to='ear_training_app.Note', null=True),
        ),
    ]
