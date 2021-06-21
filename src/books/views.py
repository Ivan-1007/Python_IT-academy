from django.shortcuts import render
from django.views.generic import UpdateView, ListView, DetailView, CreateView, DeleteView 
from django.urls import reverse_lazy
from . import models
from . import forms


# Create your views here.

class BookListView(ListView):
    model = models.Book

class BookCreateView(CreateView):
    model = models.Book
    form_class = forms.BookForm

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({'title': 'Создать книгу'})
        return cnt


class BookDetailView(DetailView):
    model = models.Book


class BookUpdateView(UpdateView):
    model = models.Book
    form_class = forms.BookForm

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({'title': 'Изменить книгу'})
        return cnt


class BookDelView(DeleteView):
    model = models.Book
    success_url = reverse_lazy('books:books',)