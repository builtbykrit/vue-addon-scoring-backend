# Generated by Django 2.2.4 on 2019-08-23 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vue_plugins', '0004_vueplugin_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vueplugin',
            old_name='num_downloads',
            new_name='num_downloads_recently',
        ),
    ]
