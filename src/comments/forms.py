from django import forms

class CreateCommentForm(forms.Form):
    comment_text = forms.CharField(required=True)
    next = forms.CharField(required=True)
    ct_id = forms.IntegerField(required=True)
    object_id = forms.IntegerField(required=True)