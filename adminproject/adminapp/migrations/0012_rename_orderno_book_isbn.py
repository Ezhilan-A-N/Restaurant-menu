# Generated by Django 3.2.7 on 2025-04-03 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0011_rename_author_tableno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='OrderNo',
            new_name='ISBN',
        ),
    ]
