# Generated by Django 2.2.4 on 2023-08-15 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SCC_app', '0020_guest_signed_out_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='signed_out_by',
            field=models.CharField(max_length=100),
        ),
    ]
