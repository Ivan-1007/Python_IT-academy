# Generated by Django 3.2.4 on 2021-06-30 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.IntegerField(max_length=9, verbose_name='Номер телефона')),
                ('country', models.CharField(blank=True, default='Беларусь', max_length=64, null=True, verbose_name='Страна')),
                ('city', models.CharField(blank=True, max_length=64, null=True, verbose_name='Город')),
                ('postcode', models.IntegerField(blank=True, max_length=6, null=True, verbose_name='Индекс')),
                ('adress_1', models.CharField(blank=True, max_length=256, null=True, verbose_name='Адрес 1')),
                ('adress_2', models.CharField(blank=True, max_length=256, null=True, verbose_name='Адрес 2')),
                ('information', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Доп. информация')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Профиль')),
            ],
        ),
    ]
