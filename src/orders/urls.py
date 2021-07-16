from django.urls import path
from . import views


app_name = 'orders'

urlpatterns = [
    path('create/', views.CreateOrderView.as_view(), name='create'),
    path('list/', views.OrderListView.as_view(), name='list'),
    path('manager-list/', views.OrderManagerListView.as_view(), name='m_list'),
    path('update/<int:pk>', views.OrderManagerUpdateView.as_view(), name='update'),
    path('cancel/<int:pk>', views.CancelOrderView.as_view(), name='cancel'),
    path('comment/<int:pk>', views.CommentOrderView.as_view(), name='comment'),
] 