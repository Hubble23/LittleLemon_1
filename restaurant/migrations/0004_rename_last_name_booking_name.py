# Generated by Django 4.2.4 on 2023-08-16 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_rename_name_booking_last_name_alter_booking_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='last_name',
            new_name='name',
        ),
    ]
