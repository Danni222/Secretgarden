# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20160506_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deliverydate',
            field=models.DateField(default=datetime.datetime(2016, 5, 7, 4, 33, 50, 509469)),
        ),
    ]
