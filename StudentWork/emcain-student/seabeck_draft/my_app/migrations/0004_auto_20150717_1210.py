# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_auto_20150716_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(max_length=4)),
                ('grade', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodPreference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meat_preference', models.TextField()),
                ('gluten_free', models.BooleanField()),
                ('dairy_free', models.BooleanField()),
                ('other', models.TextField()),
                ('severity', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ShirtOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attendance', models.ForeignKey(to='my_app.Attendance')),
            ],
        ),
        migrations.RemoveField(
            model_name='camper',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='camper',
            name='shirt_size_key',
        ),
        migrations.RemoveField(
            model_name='shirt',
            name='size_name',
        ),
        migrations.AddField(
            model_name='shirt',
            name='number_required',
            field=models.IntegerField(default=0, max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='camper',
            name='dob',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='shirt',
            name='shirt_size_key',
            field=models.IntegerField(max_length=2),
        ),
        migrations.AddField(
            model_name='shirtorder',
            name='shirt',
            field=models.ForeignKey(to='my_app.Shirt'),
        ),
        migrations.AddField(
            model_name='foodpreference',
            name='camper',
            field=models.ForeignKey(to='my_app.Camper'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='camper',
            field=models.ForeignKey(to='my_app.Camper'),
        ),
    ]
