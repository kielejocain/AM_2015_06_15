# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('auction_start_date', models.DateTimeField(auto_now_add=True)),
                ('auction_end_date', models.DateTimeField()),
                ('opening_bid', models.DecimalField(default=1.0, max_digits=7, decimal_places=2)),
                ('price', models.DecimalField(default=0.0, max_digits=7, decimal_places=2)),
                ('increment', models.DecimalField(default=1.0, max_digits=7, decimal_places=2)),
                ('auction_ended', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bid_amount', models.DecimalField(default=1.0, max_digits=7, decimal_places=2)),
                ('auction', models.ForeignKey(to='auction.Auction')),
                ('bidder', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['bid_amount'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('seller', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='auction',
            name='item',
            field=models.ForeignKey(to='auction.Item'),
        ),
    ]
