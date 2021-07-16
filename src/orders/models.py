from django.db import models
from django.db.models import deletion
from django.db.models.fields import CharField
from carts.models import Cart


class OrderStatus(models.Model):
    name = CharField(
        verbose_name='Название',
        max_length=128,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'





class Order(models.Model):   
    cart = models.OneToOneField(
        Cart,
        verbose_name='Заказ',
        on_delete=models.PROTECT,
        related_name='order',   
    )
    phone_number = models.IntegerField(
        verbose_name='Номер телефона',
    )
    created = models.DateTimeField(verbose_name = "Дата внесения в каталог", auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(verbose_name = "Дата последнего редактирования в БД", auto_now=True, auto_now_add=False)
    status= models.ForeignKey(
        OrderStatus,
        verbose_name='Статус',
        related_name='orders',
        on_delete=models.PROTECT,
    )
    information = models.TextField(verbose_name='Доп. информация', blank=True, null=True,) 

    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'