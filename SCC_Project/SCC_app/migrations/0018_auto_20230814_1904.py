# Generated by Django 2.2.4 on 2023-08-14 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SCC_app', '0017_auto_20230814_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='client',
            field=models.CharField(max_length=100),
        ),
    ]
