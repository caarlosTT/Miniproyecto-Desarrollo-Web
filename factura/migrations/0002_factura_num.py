# Generated by Django 3.2.3 on 2021-06-17 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='num',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
