# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20160501_2231'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='flower',
            unique_together=set([('productID', 'flowertype', 'flowercolor', 'flowerdiyocategory')]),
        ),
    ]
