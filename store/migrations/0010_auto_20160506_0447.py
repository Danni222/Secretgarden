# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20160506_0440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deliverydate',
            field=models.DateField(default=datetime.datetime(2016, 5, 7, 9, 47, 10, 455999, tzinfo=utc)),
        ),
    ]
