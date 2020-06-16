# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0006_blog_blog_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blog_photo',
            new_name='image',
        ),
    ]
