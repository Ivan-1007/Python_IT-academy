# Generated by Django 3.2.4 on 2021-07-05 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0006_auto_20210705_0926'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.IntegerField(verbose_name='Номер телефона')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата внесения в каталог')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата последнего редактирования в БД')),
                ('information', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order', to='carts.cart', verbose_name='Заказ')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='orders.orderstatus', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
