from django.urls import path
from . import views


app_name = 'books'

urlpatterns = [   
    path('', views.BookListView.as_view(), name='books'),
    path('book-create/', views.BookCreateView.as_view(), name='create'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book'),
    path('book-upd/<int:pk>', views.BookUpdateView.as_view(), name='update'),
    path('book-del/<int:pk>', views.BookDelView.as_view(), name='del'),
    
]