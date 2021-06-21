"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from proj import settings

from django.http import HttpResponseRedirect
from django.urls import reverse



def redirect_to_books(request):
    return HttpResponseRedirect(reverse('books:books'))


urlpatterns = [
    path('admin/', admin.site.urls),
    path('directories/', include('directories.urls', namespace='dirs')),
    path('books/', include('books.urls', namespace='books')),
    path('users/', include('users.urls', namespace='users')),
    path('', redirect_to_books, name='main'),

] 


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),