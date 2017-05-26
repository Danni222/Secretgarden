# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_auto_20160506_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(choices=[('McAllen', 'McAllen'), ('Edinburg', 'Edinburg'), ('Mission', 'Mission')], verbose_name='City', max_length=100, default=None),
        ),
        migrations.AlterField(
            model_name='order',
            name='deliverydate',
            field=models.DateField(verbose_name='date', default=datetime.datetime(2016, 5, 7, 22, 27, 29, 602532, tzinfo=utc)),
        ),
    ]
