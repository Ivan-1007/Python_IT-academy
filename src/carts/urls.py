from django.urls import path
from . import views


app_name = 'carts'

urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    path('delete-book/<int:pk>', views.BookInCartDeleteView.as_view(), name='del_book'),
    path('update-cart', views.UpdateCartView.as_view(), name='upd_cart'),
]