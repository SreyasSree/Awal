# Generated by Django 4.1.3 on 2022-12-09 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_remove_order_phone_remove_order_customer_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]
