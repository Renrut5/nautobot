# Generated by Django 3.2.18 on 2023-05-09 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0079_tagsfield'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relationship',
            old_name='slug',
            new_name='key',
        ),
    ]
