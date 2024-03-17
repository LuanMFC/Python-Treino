# Generated by Django 5.0.1 on 2024-01-19 00:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('brand_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='car',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False)),
                ('car_name', models.CharField(max_length=200)),
                ('car_color', models.CharField(max_length=200)),
                ('car_price', models.FloatField()),
                ('car_year', models.IntegerField()),
                ('car_mileage', models.IntegerField()),
                ('car_brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cars_brands', to='cars.brand')),
            ],
        ),
    ]