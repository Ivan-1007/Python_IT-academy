# Generated by Django 3.2.4 on 2021-06-12 21:54

import books.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('directories', '0007_series'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Имя')),
                ('discription', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('picture', models.ImageField(default='authors/Author', upload_to=books.models.book_directory_path, verbose_name='Изображение')),
                ('price', models.FloatField(verbose_name='цена (BYN)')),
                ('pyblishing_year', models.IntegerField(blank=True, null=True, verbose_name='год издания')),
                ('pages', models.IntegerField(blank=True, null=True, verbose_name='страниц')),
                ('binding', models.CharField(choices=[('T', 'твердый'), ('М', 'мягкий'), ('др', 'другой')], default='др', max_length=2, verbose_name='переплет')),
                ('format', models.CharField(choices=[('св_кр', 'сверхкрупная (84×108/16; 70×90/8)'), ('кр', 'крупная (70×90/16; 75×90/16)'), ('ср', 'средняя (60×90/16; 84×108/32)'), ('мал', 'малая (70×90/32; 70×108/32)'), ('св_м', 'сверхмалая (60×90/32)')], default='ср', max_length=5, verbose_name='формат')),
                ('ISBN', models.CharField(blank=True, max_length=17, null=True, verbose_name='ISBN номер')),
                ('weight', models.IntegerField(blank=True, null=True, verbose_name='вес, (гр.)')),
                ('age_restrictions', models.CharField(default='нет', max_length=3, verbose_name='возрастные ограничения')),
                ('in_stock', models.IntegerField(blank=True, null=True, verbose_name='кол-во в наличии')),
                ('available', models.BooleanField(default=False, verbose_name='доступна для заказа')),
                ('rating', models.FloatField(blank=True, null=True, verbose_name='рейтинг')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата внесения в каталог')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата последнего редактирования в БД')),
                ('authors', models.ManyToManyField(related_name='books', to='directories.Author')),
                ('genre', models.ManyToManyField(related_name='books', to='directories.Genre', verbose_name='жанры')),
                ('ph', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='directories.publishinghouse')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='directories.series', verbose_name='серия')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
    ]
