# Generated by Django 5.2.1 on 2025-06-03 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_rename_fisrt_mame_member_first_mame'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='first_mame',
            new_name='first_name',
        ),
    ]
