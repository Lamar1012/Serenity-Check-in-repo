# Generated by Django 2.2.4 on 2023-08-17 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SCC_app', '0023_auto_20230817_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='signed_in',
            field=models.DateField(auto_now=True),
        ),
    ]
