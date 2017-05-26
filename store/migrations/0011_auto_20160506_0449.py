# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20160506_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deliverydate',
            field=models.DateField(default=datetime.datetime(2016, 5, 7, 9, 49, 27, 570951, tzinfo=utc)),
        ),
    ]
