# Generated by Django 3.1.7 on 2021-03-08 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='play',
            old_name='spotify_Link',
            new_name='amazon_Link',
        ),
    ]
