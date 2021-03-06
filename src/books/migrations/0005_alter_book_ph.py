# Generated by Django 3.2.4 on 2021-06-16 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0008_alter_author_picture'),
        ('books', '0004_auto_20210613_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ph',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='books', to='directories.publishinghouse', verbose_name='Издательство'),
        ),
    ]
