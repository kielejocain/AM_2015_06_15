# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20150715_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shirt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.RenameField(
            model_name='camper',
            old_name='shirt_size',
            new_name='shirt_size_key',
        ),
        migrations.AddField(
            model_name='shirt',
            name='shirt_size_key',
            field=models.ForeignKey(to='my_app.Camper'),
        ),
    ]
