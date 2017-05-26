# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20160506_0453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='deliverydate',
        ),
    ]
