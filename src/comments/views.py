from django.views.generic import FormView
from .forms import CreateCommentForm
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from .models import Comment
from django.contrib import messages

# Create your views here.

class CreateCommentView(FormView):
    form_class = CreateCommentForm
    def form_valid(self, form):
        try:
            data = form.cleaned_data
            next = data.get('next')
            comment_text = data.get('comment_text')
            author = self.request.user
            ct_id = data.get('ct_id')
            ct = ContentType.objects.get(pk=ct_id)
            o_id = data.get('object_id')
        
            Comment.objects.create(
                author=author,
                text=comment_text,
                content_type = ct,
                object_id = o_id,
            )
        except BaseException:
            messages.add_message(self.request, messages.WARNING, f'{self.request.user}, Произошла ошибка! Ваш коментарий не добавлен!')
            
        return HttpResponseRedirect('books/manager-list/')