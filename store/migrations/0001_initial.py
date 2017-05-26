# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bestseller', models.BooleanField(default=False)),
                ('collectiontype', models.CharField(choices=[('Birthday', 'Birthday'), ('Anniversary', 'Anniversary'), ('Sympathy', 'Sympathy')], max_length=100, verbose_name='Collection Type', default=None)),
                ('updatedDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('fname', models.CharField(max_length=30, verbose_name='First Name')),
                ('lname', models.CharField(max_length=30, verbose_name='Last Name')),
                ('email', models.EmailField(primary_key=True, max_length=254, verbose_name='Email', serialize=False)),
                ('phoneNumber', models.CharField(max_length=12, verbose_name='phoneNumber')),
                ('password', models.CharField(max_length=100, verbose_name='Password', help_text='Please use at least one uppercase and a number')),
                ('registeredDate', models.DateTimeField(auto_now_add=True)),
                ('updatedDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('flowertype', models.CharField(choices=[('Rose', 'Rose'), ('Lily', 'Lily'), ('Tulip', 'Tulip'), ('Calla Lily', 'Calla Lily'), ('Gilly Flower', 'Gilly Flower'), ('Sunflower', 'Sunflower'), ('Peruvian Lily', 'Peruvian Lily'), ('Gerbera Daisies', 'Gerbera Daisies')], max_length=100, verbose_name='Flower Type', default=None)),
                ('flowercolor', models.CharField(choices=[('Red', 'Red'), ('White', 'White'), ('Pink', 'Pink'), ('Yellow', 'Yellow'), ('Purple', 'Purple'), ('Orange', 'Orange'), ('More Than one', 'More Than One')], max_length=100, verbose_name='Flower Color', default=None)),
                ('flowerdiyocategory', models.CharField(choices=[('Romantic Love', 'Romantic Love'), ('Friendship', 'Friendship'), ('Family', 'Family')], max_length=100, verbose_name='Category', default=None)),
                ('updatedDate', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderID', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=250, verbose_name='Address', default=None)),
                ('postalCode', models.CharField(max_length=20, verbose_name='Zip Code', default=None)),
                ('city', models.CharField(max_length=100, verbose_name='City', default=None)),
                ('state', models.CharField(max_length=100, verbose_name='State', default=None)),
                ('makebouquet', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('orderItemID', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('orderID', models.ForeignKey(related_name='items', to='store.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productID', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('productname', models.CharField(max_length=50, verbose_name='ProductName')),
                ('productdescription', models.CharField(max_length=300, verbose_name='ProductDescription')),
                ('productprice', models.DecimalField(decimal_places=2, max_digits=7)),
                ('productimage', models.ImageField(upload_to='product')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='orderitem',
            name='productID',
            field=models.ForeignKey(related_name='order_items', to='store.Product'),
        ),
        migrations.AddField(
            model_name='flower',
            name='productID',
            field=models.ForeignKey(to='store.Product'),
        ),
        migrations.AddField(
            model_name='collection',
            name='productID',
            field=models.ForeignKey(to='store.Product'),
        ),
        migrations.AlterUniqueTogether(
            name='flower',
            unique_together=set([('productID', 'flowertype')]),
        ),
        migrations.AlterUniqueTogether(
            name='collection',
            unique_together=set([('productID', 'collectiontype')]),
        ),
    ]
