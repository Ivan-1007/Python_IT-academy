from django.urls import path
from . import views


app_name = 'books'

urlpatterns = [
    path('main/', views.BookListMainPageView.as_view(), name='main'),

    path('', views.BookListView.as_view(), name='books'),
    path('book-create/', views.BookCreateView.as_view(), name='create'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book'),
    path('book-upd/<int:pk>', views.BookUpdateView.as_view(), name='update'),
    path('book-del/<int:pk>', views.BookDelView.as_view(), name='del'),
    path('import-CSV', views.ImportCSVView.as_view(), name='import_CSV'),

    path('manager-list/', views.BookManagerListView.as_view(), name='books_manager'),
    
]