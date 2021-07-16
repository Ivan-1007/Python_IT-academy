from django.contrib.auth.models import GroupManager
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name='Профиль',
        on_delete=models.CASCADE,
        related_name='profile'
    )

    phonenumber = models.IntegerField(
        verbose_name='Номер телефона',
    )

    country = models.CharField(
        verbose_name='Страна',
        max_length=64,
        default='Беларусь',
        blank=True, null=True,
    )

    city = models.CharField(
        verbose_name='Город',
        max_length=64,
        blank=True, null=True,
    )
    
    postcode = models.IntegerField(
        verbose_name='Индекс',
        blank=True, null=True,
    )

    adress_1 = models.CharField(
        verbose_name='Адрес 1',
        max_length=256,
        blank=True, null=True,
    )

    adress_2 = models.CharField(
        verbose_name='Адрес 2',
        max_length=256,
        blank=True, null=True,
    )

    information = models.CharField(
        verbose_name='Доп. информация',
        max_length=1024,
        blank=True, null=True,  
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'



