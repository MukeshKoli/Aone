# Generated by Django 2.0 on 2018-12-28 14:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20181228_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='orderDate',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 28, 14, 46, 15, 772384, tzinfo=utc), verbose_name='Date'),
        ),
    ]
