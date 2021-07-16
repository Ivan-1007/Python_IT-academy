from django import forms
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from .models import Profile

            
User = get_user_model()
username_validator = UnicodeUsernameValidator()

def repeat_name_validator(name):
    try:    
        result = User.objects.get(username=name)
    except User.DoesNotExist:
        result = False

    if result:    
        raise ValidationError(
            f'Пользователь с именем {name} уже существует.',
            code='invalid',
            params={'value': name},
        )


class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length='150',
        required=True,
        label='Имя пользователя',
        validators=[username_validator, repeat_name_validator],
        error_messages={
            'unique': 'Не допустимый логин.',
        }
    )
     
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    
    password2 = forms.CharField(
        label='Проверка пароля',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    phone_number = forms.CharField(
        required=True,
        label='Номер телефона (хх)ххх-хх-хх',
        validators=(RegexValidator(r'^(29|33|25|44)[1-9][0-9]{6}$', 'Не верный номер телефона.'),),
        help_text='Пример: 291234567'
    )

    email = forms.EmailField(
        required=True,
        label='Электронная почта',
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                'Пароли не совпадают',
                code='password_mismatch',
            )
        try:
            validate_password(password2, User)
        except ValidationError as error:
            self.add_error('password2', error)
        return password2


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'phonenumber',
            'country',
            'city',
            'postcode',
            'adress_1',
            'adress_2',
            'information',
        ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]