from django.shortcuts import render

from .models import *
from . import forms 
from django.views.generic import UpdateView, ListView, DetailView, CreateView, DeleteView, TemplateView
from django.urls import reverse_lazy

# Create your views here.


# class Home(TemplateView):
#     template_name = 'bookshop/index.html'

# Genre (CRUDL)
class AuthorCreate(CreateView):
    model = Author
    form_class = forms.AuthorForm
    template_name = 'directories/dir_item_form.html'

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({'title': 'Создать автора'})
        return cnt


class AuthorDetail(DetailView):
    model = Author
    template_name = 'directories/dir_item.html'

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({
            'back_link': reverse_lazy('dirs:authors'),
            'url_upd': 'dirs:author_upd',
            'url_del': 'dirs:author_del',
            })
        return cnt


class AuthorUpdate(UpdateView):
    model = Author
    form_class = forms.AuthorForm
    template_name = 'directories/dir_item_form.html'

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({'title': 'Изменить автора'})
        return cnt


class AuthorDel(DeleteView):
    model = Author
    template_name = 'directories/dir_item_del.html'
    success_url = reverse_lazy('dirs:authors')

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({'title': 'Удалить автора', 'back_link': reverse_lazy('dirs:authors')})
        return cnt


class AuthorsList(ListView):
    model = Author
    template_name = 'directories/dir_list.html'

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({
            'title': 'Авторы',
            'url_det': 'dirs:author',
            'url_upd': 'dirs:author_upd',
            'url_del': 'dirs:author_del',
            'url_create': 'dirs:author_create',
            })
        return cnt



# Genre (CRUDL)
class GenreCreate(CreateView):
    model = Genre
    form_class = forms.GenreForm
    template_name = 'directories/dir_item_form.html'

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({'title': 'Создать жанр'})
        return cnt


class GenreDetail(DetailView):
    model = Genre
    template_name = 'directories/dir_item.html'

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({
            'back_link': reverse_lazy('dirs:genres'),
            'url_upd': 'dirs:genre_upd',
            'url_del': 'dirs:genre_del',
            })
        return cnt


class GenreUpdate(UpdateView):
    model = Genre
    form_class = forms.GenreForm
    template_name = 'directories/dir_item_form.html'

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({'title': 'Изменить жанр'})
        return cnt


class GenreDel(DeleteView):
    model = Genre
    template_name = 'directories/dir_item_del.html'
    success_url = reverse_lazy('dirs:genres')

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({'title': 'Удалить жанр', 'back_link': reverse_lazy('dirs:genres')})
        return cnt


class GenresList(ListView):
    model = Genre
    template_name = 'directories/dir_list.html'

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({
            'title': 'Жанры',
            'url_det': 'dirs:genre',
            'url_upd': 'dirs:genre_upd',
            'url_del': 'dirs:genre_del',
            'url_create': 'dirs:genre_create',
            })
        return cnt


# Publ house (CRUDL)
class PhCreate(CreateView):
    model = PublishingHouse
    form_class = forms.PhForm
    template_name = 'directories/dir_item_form.html'

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({'title': 'Добавить издательство'})
        return cnt


class PhDetail(DetailView):
    model = PublishingHouse
    template_name = 'directories/dir_item.html'

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({
            'back_link': reverse_lazy('dirs:phs'),
            'url_upd': 'dirs:ph_upd',
            'url_del': 'dirs:ph_del',
            })
        return cnt


class PhUpdate(UpdateView):
    model = PublishingHouse
    form_class = forms.PhForm
    template_name = 'directories/dir_item_form.html'

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({'title': 'Редактировать издательство'})
        return cnt


class PhDel(DeleteView):
    model = PublishingHouse
    template_name = 'directories/dir_item_del.html'
    success_url = reverse_lazy('dirs:phs')

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({'title': 'Удалить издательство', 'back_link': reverse_lazy('dirs:phs')})
        return cnt


class PhList(ListView):
    model = PublishingHouse
    template_name = 'directories/dir_list.html'

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({
            'title': 'Издательства',
            'url_det': 'dirs:ph',
            'url_upd': 'dirs:ph_upd',
            'url_del': 'dirs:ph_del',
            'url_create': 'dirs:ph_create',
            })
        return cnt


# Series (CRUDL)
class SeriesCreate(CreateView):
    model = Series
    form_class = forms.SeriesForm
    template_name = 'directories/dir_item_form.html'

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({'title': 'Добавить серию'})
        print(cnt)
        return cnt


class SeriesDetail(DetailView):
    model = Series
    template_name = 'directories/dir_item.html'

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({
            'back_link': reverse_lazy('dirs:series_list'),
            'url_upd': 'dirs:series_upd',
            'url_del': 'dirs:series_del',
            })
        print(cnt)
        return cnt


class SeriesUpdate(UpdateView):
    model = Series
    form_class = forms.SeriesForm
    template_name = 'directories/dir_item_form.html'

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({'title': 'Редактировать серию'})
        return cnt


class SeriesDel(DeleteView):
    model = Series
    template_name = 'directories/dir_item_del.html'
    success_url = reverse_lazy('dirs:series_list')

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({'title': 'Удалить серию', 'back_link': reverse_lazy('dirs:series_list')})
        return cnt


class SeriesList(ListView):
    model = Series
    template_name = 'directories/dir_list.html'

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({
            'title': 'Серии',
            'url_det': 'dirs:series',
            'url_upd': 'dirs:series_upd',
            'url_del': 'dirs:series_del',
            'url_create': 'dirs:series_create',
            })
        return cnt

