# Generated by Django 5.0.1 on 2024-01-18 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('car_year', models.IntegerField()),
                ('car_mileage', models.IntegerField()),
                ('car_price', models.FloatField()),
            ],
        ),
    ]
