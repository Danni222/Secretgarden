# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20160501_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='state',
        ),
    ]
