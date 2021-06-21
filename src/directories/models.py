from django.db import models
from django.urls import reverse

def author_directory_path(instance, filename):
    return f'authors/{instance.name}'
class Author(models.Model):

    name = models.CharField(verbose_name='Имя', max_length=30, )
    discription = models.TextField(verbose_name='Описание', blank=True, null=True,)
    picture = models.ImageField(verbose_name='Изображение', upload_to=author_directory_path, default='authors/Author.png')

    def __str__(self) -> str: 
        return f'{self.name}, {self.discription[:15]}...'
    
    def get_absolute_url(self):
        return reverse('dirs:author', args=[self.pk])   #  можно так  bookshop:author, args=[self.pk]
        
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Genre(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=30,)
    discription = models.TextField(verbose_name='Описание', blank=True, null=True,)

    def __str__(self) -> str:
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('dirs:genres')
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class PublishingHouse(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50,)

    def __str__(self) -> str:
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('dirs:phs')

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'


class Series(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50, )

    def __str__(self) -> str:
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('dirs:series_list')

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'