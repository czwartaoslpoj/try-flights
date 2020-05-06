# Generated by Django 2.0.3 on 2020-05-06 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flights', '0002_auto_20200505_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='Flights.Flight')),
            ],
        ),
    ]
