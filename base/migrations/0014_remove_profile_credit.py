# Generated by Django 4.0.6 on 2022-11-15 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_remove_profile_usertype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='credit',
        ),
    ]
