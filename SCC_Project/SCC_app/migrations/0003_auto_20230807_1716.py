# Generated by Django 2.2.4 on 2023-08-07 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SCC_app', '0002_auto_20230805_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
