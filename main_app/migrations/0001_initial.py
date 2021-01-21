# Generated by Django 3.1.5 on 2021-01-21 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.CharField(blank=True, max_length=1000)),
                ('photo', models.ImageField(default='static/assets/icons/user-solid.svg', upload_to='images/')),
                ('website', models.URLField(blank=True, max_length=1000)),
                ('facebook', models.URLField(blank=True, max_length=1000)),
                ('twitter', models.URLField(blank=True, max_length=1000)),
                ('instagram', models.URLField(blank=True, max_length=1000)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=1000)),
                ('audioFile', models.FileField(upload_to='audio/')),
                ('image', models.ImageField(default='static/assets/artwork/thereordering_cassietaggart.jpg', upload_to='images/')),
                ('external_Link', models.URLField(max_length=1000)),
                ('date_Added', models.DateTimeField(auto_now_add=True)),
                ('actors', models.ManyToManyField(related_name='actors', to='main_app.Actor')),
            ],
            options={
                'ordering': ['-date_Added'],
            },
        ),
    ]
