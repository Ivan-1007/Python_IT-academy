from django.urls import path
from . import views


app_name = 'comments'

urlpatterns = [
    path('create', views.CreateCommentView.as_view(), name='create'),
]