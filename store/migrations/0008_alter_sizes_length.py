# Generated by Django 5.0.1 on 2024-08-14 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_product_discount_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sizes',
            name='length',
            field=models.CharField(max_length=20),
        ),
    ]
