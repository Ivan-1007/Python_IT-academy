from django import forms
from .models import Book 


class BookForm(forms.ModelForm):
    class Meta:
        model = Book 
        fields = '__all__'


class ImportCSVForm(forms.Form):
    csv_file = forms.FileField(required=True)
    next = forms.CharField(required=True)
    


