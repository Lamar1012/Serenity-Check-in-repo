# Generated by Django 2.2.4 on 2023-08-10 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SCC_app', '0012_auto_20230809_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='password_confirmation',
            field=models.CharField(max_length=225),
        ),
    ]