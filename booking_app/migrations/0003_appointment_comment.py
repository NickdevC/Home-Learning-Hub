# Generated by Django 3.2.16 on 2023-02-06 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0002_alter_appointment_teacher_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='comment',
            field=models.TextField(default=None),
        ),
    ]
