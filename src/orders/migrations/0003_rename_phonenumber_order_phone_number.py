# Generated by Django 3.2.4 on 2021-07-05 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='phonenumber',
            new_name='phone_number',
        ),
    ]
