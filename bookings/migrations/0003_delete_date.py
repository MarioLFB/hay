# Generated by Django 5.0.6 on 2024-06-25 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Date',
        ),
    ]
