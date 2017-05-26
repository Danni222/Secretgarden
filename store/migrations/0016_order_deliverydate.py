# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_remove_order_deliverydate'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='deliverydate',
            field=models.DateField(default=datetime.datetime(2016, 5, 7, 21, 0, 35, 256527, tzinfo=utc)),
        ),
    ]
