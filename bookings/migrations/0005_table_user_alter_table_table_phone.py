# Generated by Django 5.0.6 on 2024-06-26 16:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_table_table_date_table_table_email_table_table_phone_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='table',
            name='table_phone',
            field=models.CharField(default='+44 20 7123 4567', max_length=100),
        ),
    ]
