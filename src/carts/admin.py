from django.contrib import admin
from .models import Cart, BookInCart

# Register your models here.
@admin.register(Cart)
class BookAdmin(admin.ModelAdmin):
    list_display = ['pk', 'customer', 'created', 'updated']


@admin.register(BookInCart)
class BookInCartAdmin(admin.ModelAdmin):
    list_display = ['pk', 'book', 'quantity', 'unit_price']
