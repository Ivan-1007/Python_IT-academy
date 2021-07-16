# Generated by Django 3.2.4 on 2021-07-01 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phonenumber',
            field=models.IntegerField(verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='postcode',
            field=models.IntegerField(blank=True, null=True, verbose_name='Индекс'),
        ),
    ]
