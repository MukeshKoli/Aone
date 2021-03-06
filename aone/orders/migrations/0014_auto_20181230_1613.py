# Generated by Django 2.0 on 2018-12-30 10:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20181229_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='orderDate',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 30, 10, 43, 57, 23539, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='orderId',
            field=models.CharField(default=5801075268, max_length=256, unique=True, verbose_name='Order ID'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='orderMonth',
            field=models.DateField(default=datetime.date(2018, 12, 30), verbose_name='Month'),
        ),
    ]
