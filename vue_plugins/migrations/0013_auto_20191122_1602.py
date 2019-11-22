# Generated by Django 2.2.4 on 2019-11-22 16:02

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vue_plugins', '0012_auto_20190823_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='vueplugin',
            name='downloads_per_day_recently',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), help_text='NPM download count per day for the last 30 days', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='vueplugin',
            name='num_commits_recently',
            field=models.IntegerField(default=0, help_text='Commit count for last 30 days'),
        ),
        migrations.AlterField(
            model_name='vueplugin',
            name='num_downloads_recently',
            field=models.IntegerField(default=0, help_text='NPM download count for last 30 days'),
        ),
    ]