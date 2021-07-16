from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE


User = get_user_model()

# Create your models here.
class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name='carts',
        verbose_name='Покупатель',
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(verbose_name = "Дата внесения в каталог", auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(verbose_name = "Дата последнего редактирования в БД", auto_now=True, auto_now_add=False)


    @property
    def cart_price(self):
        books_in_cart_queryset = self.books_in_cart.all()
        cart_price = 0
        for books in books_in_cart_queryset:
            cart_price += books.total_price
        return cart_price
    def __str__(self):
        return f'id {self.pk}'

class BookInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        related_name='books_in_cart',
        verbose_name='Корзина',
        on_delete = models.CASCADE,
    )

    book = models.ForeignKey(
        'books.Book',
        on_delete=models.PROTECT,
        verbose_name='Книга', 
        related_name='books_in_cart',   
    )

    quantity = models.IntegerField(
        verbose_name='Количество',
        default=1,
    )

    unit_price = models.DecimalField(
        verbose_name='Цена за шт.',
        max_digits=6,
        decimal_places=2,
    )

    @property
    def total_price(self):
        return self.unit_price * self.quantity


