# Generated by Django 2.0 on 2018-12-30 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20181230_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='orderId',
            field=models.CharField(max_length=256, unique=True, verbose_name='Order ID'),
        ),
    ]
