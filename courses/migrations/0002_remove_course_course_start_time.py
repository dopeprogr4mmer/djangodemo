# Generated by Django 2.0.7 on 2020-04-11 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_start_time',
        ),
    ]