# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djmmdemo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('stage_name', models.CharField(max_length=255)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='playlist',
            name='performer',
            field=models.ForeignKey(default=1, to='djmmdemo_app.Performer'),
            preserve_default=False,
        ),
    ]
