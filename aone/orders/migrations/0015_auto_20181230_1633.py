# Generated by Django 2.0 on 2018-12-30 11:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20181230_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='orderDate',
            field=models.DateField(default=datetime.date(2018, 12, 30), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='orderId',
            field=models.CharField(default=9450966282, max_length=256, unique=True, verbose_name='Order ID'),
        ),
    ]
