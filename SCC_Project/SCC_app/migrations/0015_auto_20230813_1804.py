# Generated by Django 2.2.4 on 2023-08-13 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SCC_app', '0014_remove_staff_password_confirmation'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='reason',
            field=models.CharField(default='DEAFULT', max_length=225),
        ),
        migrations.AddField(
            model_name='guest',
            name='vehicle_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]