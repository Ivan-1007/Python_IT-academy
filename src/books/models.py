from django.db import models
from directories import models as dirs_models
from django.urls import reverse

# Create your models here.

def book_directory_path(instance, filename):
    return f'books/{instance.name}'


class Book(models.Model):
    
    BINDING = [
        ('T', 'твердый'),
        ('М', 'мягкий'),
        ('др', 'другой'),
    ]

    FORMAT = [
        ('св_кр', 'сверхкрупная (84×108/16; 70×90/8)'),
        ('кр', 'крупная (70×90/16; 75×90/16)'),
        ('ср', 'средняя (60×90/16; 84×108/32)'),
        ('мал', 'малая (70×90/32; 70×108/32)'),
        ('св_м', 'сверхмалая (60×90/32)'),
    ]

    name = models.CharField(verbose_name='Имя', max_length=60, )
    discription = models.TextField(verbose_name='Описание', blank=True, null=True,)
    picture = models.ImageField(verbose_name='Изображение', upload_to=book_directory_path, blank=True, default='Books/book0.png')
    price = models.FloatField(verbose_name='цена (BYN)')
    author = models.ManyToManyField(to=dirs_models.Author, related_name='books')          # Автор
    series = models.ForeignKey(to=dirs_models.Series, verbose_name='серия', related_name='books', blank=True, null=True, on_delete=models.PROTECT)  # Серии
    genre = models.ManyToManyField(to=dirs_models.Genre, verbose_name='жанры', related_name='books',)    # Жанр
    pyblishing_year = models.IntegerField(verbose_name='год издания', blank=True, null=True, )
    pages = models.IntegerField(verbose_name='страниц', blank=True, null=True, )
    binding = models.CharField(verbose_name='переплет', max_length=2, choices=BINDING, default='др')
    format = models.CharField(verbose_name='формат', max_length=5, choices=FORMAT, default='ср')
    ISBN = models.CharField(verbose_name='ISBN номер', max_length=17, blank=True, null=True,)
    weight = models.IntegerField(verbose_name='вес, (гр.)', blank=True, null=True,)
    age_restrictions = models.CharField(verbose_name='возрастные ограничения', max_length=3, default='нет')
    ph = models.ForeignKey(to=dirs_models.PublishingHouse, verbose_name='Издательство', blank=True, null=True, related_name='books', on_delete=models.PROTECT) # издательства
    in_stock = models.IntegerField(verbose_name='кол-во в наличии',  blank=True, null=True,)
    available = models.BooleanField(verbose_name='доступна для заказа', default=False)
    rating = models.FloatField(verbose_name='рейтинг', blank=True, null=True,)
    created = models.DateTimeField(verbose_name = "Дата внесения в каталог", auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(verbose_name = "Дата последнего редактирования в БД", auto_now=True, auto_now_add=False)


    def __str__(self) -> str: 
        return f'{self.name}, {self.authors}'
    
    def get_absolute_url(self):
        return reverse('books:book', args=[self.pk])   #  можно так  bookshop:author, args=[self.pk]
        
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
