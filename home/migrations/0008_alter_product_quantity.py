# Generated by Django 4.1.3 on 2022-11-30 10:22

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('1', '1'), ('2', '2'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], max_length=2),
        ),
    ]