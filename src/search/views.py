from django.forms.forms import Form
from django.views.generic import ListView
from books.models import Book
from directories.models import Author

# Create your views here.
class SearchView(ListView):
    model = Book
    template_name = 'search/list.html'

    def get_context_data(self, **kwargs):
        search = self.request.GET.get('search')
        if search == '':
            return
        cnt = {}
        cnt['books'] = Book.objects.all().filter(name__icontains=search.capitalize() )
        cnt['authors'] = Author.objects.all().filter(name__icontains=search.capitalize() )
        cnt.update({
            'url_det': 'dirs:author',
        })
        print(cnt)

        return cnt
