# Generated by Django 3.2.3 on 2021-06-17 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0005_alter_factura_fecha_emision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='anio',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='factura',
            name='num',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='lineafactura',
            name='precio_unitario',
            field=models.PositiveIntegerField(),
        ),
    ]
