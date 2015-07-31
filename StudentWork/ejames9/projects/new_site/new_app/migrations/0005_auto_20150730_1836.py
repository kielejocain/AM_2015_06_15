# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('new_app', '0004_auto_20150724_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfiles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_logo', models.ImageField(null=True, upload_to=b'user_logo/', blank=True)),
                ('join_date', models.DateTimeField(verbose_name=b'date joined')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='account',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.AddField(
            model_name='blog',
            name='user_profile',
            field=models.ForeignKey(to='new_app.UserProfiles', null=True),
        ),
    ]
