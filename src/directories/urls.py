from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'dirs'

urlpatterns = [
    path('', views.TemplateView.as_view(template_name='directories/index.html'), name='dir_lists'),
    
    path('authors', views.AuthorsList.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetail.as_view(), name='author'),
    path('author-upd/<int:pk>', views.AuthorUpdate.as_view(), name='author_upd'),
    path('author-del/<int:pk>', views.AuthorDel.as_view(), name='author_del'),
    path('author-create/', views.AuthorCreate.as_view(), name='author_create'),

    path('genres', views.GenresList.as_view(), name='genres'),
    path('genre/<int:pk>', views.GenreDetail.as_view(), name='genre'),
    path('genre-upd/<int:pk>', views.GenreUpdate.as_view(), name='genre_upd'),
    path('genre-del/<int:pk>', views.GenreDel.as_view(), name='genre_del'),
    path('genre-create/', views.GenreCreate.as_view(), name='genre_create'),
    
    path('publishing-houses', views.PhList.as_view(), name='phs'),
    path('publishing-house/<int:pk>', views.PhDetail.as_view(), name='ph'),
    path('publishing-house-upd/<int:pk>', views.PhUpdate.as_view(), name='ph_upd'),
    path('publishing-house-del/<int:pk>', views.PhDel.as_view(), name='ph_del'),
    path('publishing-house-create/', views.PhCreate.as_view(), name='ph_create'),
    
    path('series', views.SeriesList.as_view(), name='series_list'),
    path('series/<int:pk>', views.SeriesDetail.as_view(), name='series'),
    path('series-upd/<int:pk>', views.SeriesUpdate.as_view(), name='series_upd'),
    path('series-del/<int:pk>', views.SeriesDel.as_view(), name='series_del'),
    path('series-create/', views.SeriesCreate.as_view(), name='series_create'),
] 