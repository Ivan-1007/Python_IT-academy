# Generated by Django 3.2.4 on 2021-06-09 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0006_alter_genre_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Серия',
                'verbose_name_plural': 'Серии',
            },
        ),
    ]
