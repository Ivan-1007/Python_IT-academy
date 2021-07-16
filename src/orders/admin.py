from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Order, OrderStatus

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'cart',
        'phone_number',
        'information', 
        'created',
        'updated',
    ]

@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
    ]