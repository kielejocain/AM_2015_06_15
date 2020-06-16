# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0002_auto_20150715_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cmt_text', models.TextField()),
                ('cmtr_name', models.CharField(max_length=20)),
                ('pub_time', models.DateTimeField(verbose_name=b'time_published')),
                ('blog', models.ForeignKey(to='new_app.Blog')),
            ],
        ),
    ]
