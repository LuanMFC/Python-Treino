# Generated by Django 5.0.1 on 2024-01-31 13:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('factory_year', models.IntegerField(blank=True, null=True)),
                ('car_year', models.IntegerField()),
                ('mileage', models.IntegerField()),
                ('plate', models.CharField(blank=True, max_length=10, null=True)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='car')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='car_brand', to='cars.brand')),
            ],
        ),
    ]
