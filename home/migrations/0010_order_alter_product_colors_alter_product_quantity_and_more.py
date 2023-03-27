# Generated by Django 4.1.3 on 2022-12-02 05:20

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_product_image2_alter_product_image3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='colors',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('GOLD', 'GOLD'), ('BLACK', 'BLACK'), ('COPPER', 'COPPER'), ('GOLD STAINLESS STEEL', 'GOLD STAINLESS STEEL'), ('SILVER STAINLESS STEEL', 'SILVER STAINLESS STEEL'), ('COPPER PAINT', 'COPPER PAINT')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('60cm*60cm', '60cm*60cm'), ('90cm*90cm', '90cm*90cm'), ('100cm*100cm', '100cm*100cm'), ('70cm*70cm', '70cm*70cm'), ('80cm*80cm', '80cm*80cm')], max_length=50),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
    ]
