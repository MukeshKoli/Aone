# Generated by Django 2.0 on 2018-12-29 05:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20181228_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='orderDate',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 29, 5, 10, 40, 176866, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='orderMonth',
            field=models.DateField(default=datetime.date(2018, 12, 29), verbose_name='Month'),
        ),
    ]
