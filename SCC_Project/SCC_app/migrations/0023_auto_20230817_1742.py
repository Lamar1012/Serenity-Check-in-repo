# Generated by Django 2.2.4 on 2023-08-17 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SCC_app', '0022_auto_20230817_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]