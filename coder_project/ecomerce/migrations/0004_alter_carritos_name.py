# Generated by Django 4.1.4 on 2023-01-08 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomerce', '0003_remove_carritos_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carritos',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]
