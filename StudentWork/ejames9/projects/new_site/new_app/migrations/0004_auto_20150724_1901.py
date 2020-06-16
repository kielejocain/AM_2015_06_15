# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=8)),
                ('join_date', models.DateTimeField(verbose_name=b'date joined')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='account',
            field=models.ForeignKey(to='new_app.Account', null=True),
        ),
    ]
