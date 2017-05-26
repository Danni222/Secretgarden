# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='producttype',
            field=models.CharField(default=None, max_length=100, choices=[('Collection', 'Collection'), ('Flower', 'Flower'), ('Plant', 'Plant'), ('Accessory', 'Accessory')], verbose_name='ProductType'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='collectiontype',
            field=models.CharField(default=None, max_length=100, choices=[('Birthday', 'Birthday'), ('Anniversary', 'Anniversary'), ('Sympathy', 'Sympathy')], verbose_name='CollectionType'),
        ),
        migrations.AlterField(
            model_name='flower',
            name='flowercolor',
            field=models.CharField(default=None, max_length=100, choices=[('Red', 'Red'), ('White', 'White'), ('Pink', 'Pink'), ('Yellow', 'Yellow'), ('Purple', 'Purple'), ('Orange', 'Orange'), ('More Than one', 'More Than One')], verbose_name='FlowerColor'),
        ),
        migrations.AlterField(
            model_name='flower',
            name='flowertype',
            field=models.CharField(default=None, max_length=100, choices=[('Rose', 'Rose'), ('Lily', 'Lily'), ('Tulip', 'Tulip'), ('Calla Lily', 'Calla Lily'), ('Gilly Flower', 'Gilly Flower'), ('Sunflower', 'Sunflower'), ('Peruvian Lily', 'Peruvian Lily'), ('Gerbera Daisies', 'Gerbera Daisies')], verbose_name='FlowerType'),
        ),
    ]
