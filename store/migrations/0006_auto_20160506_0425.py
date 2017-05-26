# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_order_makebouquet'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='deliverydate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='makebouquet',
            field=models.BooleanField(default=False),
        ),
    ]
