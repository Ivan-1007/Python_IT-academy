from django import template
from django.contrib.contenttypes.models import ContentType
from ..models import Comment
register = template.Library()

@register.inclusion_tag('comments/comments.html', takes_context=True)
def show_comments(context):
    obj = context.get('object')
    ct = ContentType.objects.get_for_model(obj)
    comments = Comment.objects.filter(content_type = ct, object_id = obj.pk)
    ct_id = ct.pk
    request = context.get('request')

    return {'object':obj,
        'comments':comments,
        'request':request,
        'ct_id':ct_id     
    }