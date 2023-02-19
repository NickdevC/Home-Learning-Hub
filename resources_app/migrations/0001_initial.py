# Generated by Django 3.2.16 on 2023-02-19 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_name', models.CharField(max_length=80)),
                ('subject', models.CharField(choices=[('0', 'English'), ('1', 'Maths'), ('2', 'History'), ('3', 'Geography'), ('4', 'Art'), ('5', 'Science'), ('6', 'Music')], default='0', max_length=80)),
                ('description', models.CharField(max_length=150)),
                ('file', models.FileField(blank=True, upload_to='media/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]