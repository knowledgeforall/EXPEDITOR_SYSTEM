# Generated by Django 3.1.4 on 2021-04-16 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_vertical_farm_1_vertical_farm_10_vertical_farm_3_vertical_farm_4_vertical_farm_5_vertical_farm_6_ver'),
    ]

    operations = [
        migrations.AddField(
            model_name='produce_orders',
            name='Vf_Order',
            field=models.CharField(default=0, max_length=45),
            preserve_default=False,
        ),
    ]
