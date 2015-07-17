# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('under_18', models.BooleanField()),
                ('dob', models.DateField()),
                ('grade', models.IntegerField()),
                ('shirt_size', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=20)),
                ('item', models.IntegerField()),
                ('cost_per', models.DecimalField(max_digits=20, decimal_places=4)),
            ],
        ),
        migrations.CreateModel(
            name='Registrant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('total_owed', models.DecimalField(max_digits=20, decimal_places=4)),
                ('total_paid', models.DecimalField(max_digits=20, decimal_places=4)),
            ],
        ),
        migrations.AddField(
            model_name='camper',
            name='registrant',
            field=models.ForeignKey(to='my_app.Registrant'),
        ),
    ]
