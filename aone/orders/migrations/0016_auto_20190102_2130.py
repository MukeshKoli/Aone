# Generated by Django 2.0 on 2019-01-02 16:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20181230_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='itemQuantity',
            field=models.CharField(blank=True, max_length=256, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='orderDate',
            field=models.DateField(default=datetime.date(2019, 1, 2), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='orderId',
            field=models.CharField(blank=True, max_length=256, unique=True, verbose_name='Order ID'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='orderMonth',
            field=models.DateField(default=datetime.date(2019, 1, 2), verbose_name='Month'),
        ),
    ]
