# Generated by Django 3.2.7 on 2025-04-03 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_auto_20250403_2351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Id',
            new_name='Title',
        ),
    ]
