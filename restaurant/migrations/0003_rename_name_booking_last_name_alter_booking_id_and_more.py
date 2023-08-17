# Generated by Django 4.2.4 on 2023-08-16 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_id_alter_menu_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='name',
            new_name='last_name',
        ),
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.IntegerField(default=11, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.IntegerField(default=5, primary_key=True, serialize=False),
        ),
    ]
