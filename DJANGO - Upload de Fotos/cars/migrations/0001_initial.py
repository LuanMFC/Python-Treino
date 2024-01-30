# Generated by Django 5.0.1 on 2024-01-19 12:06

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
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('year', models.IntegerField(null=True)),
                ('mileage', models.IntegerField(null=True)),
                ('plate', models.CharField(max_length=10, null=True)),
                ('price', models.FloatField(null=True)),
                ('photo', models.ImageField(upload_to='cars/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='car_brand', to='cars.brand')),
            ],
        ),
    ]