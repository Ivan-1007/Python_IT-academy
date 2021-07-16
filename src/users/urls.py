from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'users'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>', views.ProfileView.as_view(), name='profile'),
    path('update-profile/<int:pk>', views.UpdateProfileView.as_view(), name='update'),


]    
    