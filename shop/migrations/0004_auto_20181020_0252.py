# Generated by Django 2.0.5 on 2018-10-20 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20181020_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('Green', 'GREEN'), ('Blue', 'BLUE'), ('Red', 'RED'), ('Orange', 'ORANGE'), ('Black', 'BLACK'), ('Yellow', 'YELLOW'), ('White', 'WHITE')], default='green', max_length=20),
        ),
    ]