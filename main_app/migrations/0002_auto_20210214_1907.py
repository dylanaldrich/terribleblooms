# Generated by Django 3.1.5 on 2021-02-14 19:07

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performer',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='performer',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='performer',
            name='twitter',
        ),
        migrations.RemoveField(
            model_name='performer',
            name='website',
        ),
        migrations.AlterField(
            model_name='performer',
            name='bio',
            field=django_quill.fields.QuillField(blank=True),
        ),
    ]