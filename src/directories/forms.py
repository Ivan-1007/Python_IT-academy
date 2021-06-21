from django import forms
from . import models


class AuthorForm(forms.ModelForm):

    class Meta:
        model = models.Author
        fields = '__all__'


class GenreForm(forms.ModelForm):

    class Meta:
        model = models.Genre
        fields = '__all__'


class PhForm(forms.ModelForm):

    class Meta:
        model = models.PublishingHouse
        fields = '__all__'


class SeriesForm(forms.ModelForm):

    class Meta:
        model = models.Series
        fields = '__all__'




