# Generated by Django 3.1.2 on 2020-12-29 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='poll_db',
            new_name='db',
        ),
    ]
