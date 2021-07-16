from django import forms
from . import models
from django.core.validators import RegexValidator


class OrderForm(forms.Form):
    phone_number = forms.CharField(
        required=True,
        label='Номер телефона (хх)ххх-хх-хх',
        validators=(RegexValidator(r'^(29|33|25|44)[1-9][0-9]{6}$', 'Не верный номер телефона.'),),
    )
    information = forms.CharField(label='Информация', required=False, help_text='Не обязательное поле.')

class OrderManagerForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ('status', 'information')



