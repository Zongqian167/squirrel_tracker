# Generated by Django 3.1.2 on 2020-10-18 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField(max_length=100)),
                ('latitude', models.FloatField(max_length=100)),
                ('unique_squirrel_id', models.CharField(max_length=200)),
                ('shift', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('age', models.CharField(max_length=200)),
            ],
        ),
    ]
