from django.shortcuts import render
from django.views.generic import UpdateView, ListView, DetailView, CreateView, DeleteView, FormView 
from django.urls import reverse_lazy
from . import models
from . import forms
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
import csv
from directories import models as dmodels


# Create your views here.

class BookListView(ListView):
    model = models.Book
    paginate_by = 16


class BookManagerListView(ListView, PermissionRequiredMixin):
    template_name = 'books/book_list_manager.html'
    model = models.Book
    login_url = '/users/login/'
    permission_required = ('books.add_book', 'books.update_book', 'books.delete_book' )
    paginate_by = 40

class BookCreateView(PermissionRequiredMixin, CreateView):
    model = models.Book
    form_class = forms.BookForm
    login_url = '/users/login/'
    permission_required = "books.add_book"

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({'title': 'Создать книгу'})
        return cnt


class BookDetailView(DetailView):
    model = models.Book


class BookUpdateView(UpdateView, PermissionRequiredMixin):
    model = models.Book
    form_class = forms.BookForm
    permission_required = 'books.update_book'

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt.update({'title': 'Изменить книгу'})
        return cnt


class BookDelView(DeleteView, PermissionRequiredMixin):
    model = models.Book
    success_url = reverse_lazy('books:books_manager',)
    permission_required = 'books.delete_book'

class BookListMainPageView(ListView):
    template_name = 'books/main.html'
    model = models.Book
    paginate_by = 4

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        new_books = models.Book.objects.all().filter(available=True).order_by('-created')[:8]
        popular_books = models.Book.objects.all().filter(available=True).order_by('-rating')[:8]
        cnt.update({
            'new_books': new_books,
            'popular_books': popular_books,
            })
        return cnt
    

class ImportCSVView(FormView):
    form_class = forms.ImportCSVForm
    success_url = reverse_lazy('books:books_manager')

    def get_authors(self, authors:str):
        Author = dmodels.Author
        authors = authors.split(',')
        result = []
        for author in authors:
            object, created = Author.objects.get_or_create(
                name=author.strip(),
                defaults={'discription':f'Тут должно быть описание {author}'},
            )
            result.append(object)
        return result

    def get_series(self, series:str):
        Series = dmodels.Series
        series, created = Series.objects.get_or_create(
                name=series.strip(),
                defaults={},
            )
        return series
    
    def get_genre(self, genres:str):
        Genre = dmodels.Genre
        genres = genres.split(',')
        result = []
        for genre in genres:
            object, created = Genre.objects.get_or_create(
                name=genre.strip(),
                defaults={'discription':f'Тут должно быть описание {genre}'},
            )
            result.append(object)
        return result

    def get_ph(self, ph:str):
        Ph = dmodels.PublishingHouse
        ph, created = Ph.objects.get_or_create(
                name=ph.strip(),
                defaults={},
            )
        return ph

    def form_valid(self, form):
        # try:
        file = self.request.FILES['csv_file'] 
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        for row in reader:
            name = row.get('name')
            discription = row.get('discription')
            price = float(row.get('price'))
            authors = row.get('authors')
            series = row.get('series')
            genre = row.get('genre')
            pyblishing_year = int(row.get('pyblishing_year'))
            pages = int(row.get('pages'))
            binding = row.get('binding')
            format = row.get('format')
            ISBN = row.get('ISBN')
            weight = int(row.get('weight'))
            age_restrictions = row.get('age_restrictions')
            ph = row.get('ph')
            in_stock = int(row.get('in_stock'))
            available = True if row.get('in_stock') == '+' else False
            rating = float(row.get('rating'))

            print(format, '**********************************************************')

            authors = self.get_authors(authors)
            if series:
                series = self.get_series(series)
            genre = self.get_genre(genre)
            ph = self.get_ph(ph)
            
            book = models.Book(name=name,
                discription=discription,
                    price=price,
                    series=series,
                    pyblishing_year=pyblishing_year,
                    pages=pages,
                    binding=binding,
                    format=format,
                    ISBN=ISBN,
                    weight=weight,
                    age_restrictions=age_restrictions,
                    ph=ph,
                    in_stock=in_stock,
                    available=available,
                    rating=rating,
            )
            book.save()
            auths = (a.pk for a in authors)
            book.authors.add(*auths)
            gs = (g.pk for g in genre)
            book.genre.add(*gs)
            book.save()

        # except BaseException:
        #     messages.add_message(self.request, messages.WARNING, f'{self.request.user}, Произошла ошибка при импорте СSV файла!')
        return super().form_valid(form)
        #  HttpResponseRedirect(reverse_lazy('books:books_manager'))




    