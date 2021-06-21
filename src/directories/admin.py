from django.contrib import admin
from .models import Author, Genre, PublishingHouse

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'discription', 'picture']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'discription',]

    
@admin.register(PublishingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name',]