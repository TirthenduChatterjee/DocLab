# Generated by Django 5.0.1 on 2024-01-23 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointment', '0003_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]