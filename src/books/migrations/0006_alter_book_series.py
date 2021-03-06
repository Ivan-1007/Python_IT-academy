# Generated by Django 3.2.4 on 2021-06-16 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0008_alter_author_picture'),
        ('books', '0005_alter_book_ph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='books', to='directories.series', verbose_name='серия'),
        ),
    ]
