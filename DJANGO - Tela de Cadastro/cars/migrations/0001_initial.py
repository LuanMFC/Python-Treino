# Generated by Django 5.0.1 on 2024-01-25 03:09

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
                ('model', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('color', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('image', models.CharField(max_length=200)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='car', to='cars.brand')),
            ],
        ),
    ]