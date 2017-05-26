# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_order_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='makebouquet',
        ),
    ]
