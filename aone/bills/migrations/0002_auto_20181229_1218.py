# Generated by Django 2.0 on 2018-12-29 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='billNumber',
            field=models.CharField(max_length=256, verbose_name='Bill no'),
        ),
    ]
