# Generated by Django 4.0.6 on 2022-11-20 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_stand_profile_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stand',
            name='profile_id',
        ),
    ]
