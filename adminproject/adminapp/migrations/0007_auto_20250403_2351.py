# Generated by Django 3.2.7 on 2025-04-03 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_rename_id_book_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Order_Number',
            new_name='ISBN',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='ID',
            new_name='Id',
        ),
    ]
