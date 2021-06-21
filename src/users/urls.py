from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'users'

urlpatterns = [
    path('login', views.Login.as_view(), name='login'),
    # path('user/<int:pk>', views.AuthorDetail.as_view(), name='detail'),
    # path('user-upd/<int:pk>', views.AuthorUpdate.as_view(), name='update'),
]    
    