# Generated by Django 3.2.7 on 2025-04-03 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_auto_20250403_2325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='OrderNumber',
            new_name='Order_Number',
        ),
    ]
