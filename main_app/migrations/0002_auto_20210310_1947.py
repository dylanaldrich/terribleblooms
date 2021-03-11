# Generated by Django 3.1.7 on 2021-03-11 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play',
            name='audioFile',
            field=models.FileField(upload_to='audio'),
        ),
        migrations.AlterField(
            model_name='play',
            name='image',
            field=models.ImageField(default='static/assets/artwork/thereordering_cassietaggart_lores.jpg', upload_to='images'),
        ),
    ]