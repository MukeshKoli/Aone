# Generated by Django 2.0 on 2018-12-27 14:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('products', '0004_remove_products_compid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderId', models.CharField(max_length=256, unique=True, verbose_name='Order ID')),
                ('orderDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date')),
                ('orderMonth', models.CharField(max_length=50, verbose_name='Month')),
                ('orderStatus', models.CharField(choices=[('In Progress', 'In Progress'), ('Billable', 'Billable'), ('Billed', 'Billed')], default='In Progress', max_length=50, verbose_name='Status')),
                ('compName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company', verbose_name='Company Name')),
                ('itemName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Products', verbose_name='Items')),
            ],
        ),
    ]
