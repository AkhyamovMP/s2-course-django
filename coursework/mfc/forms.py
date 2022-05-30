from pyexpat import model
from attr import field
from django.forms import ModelForm, PasswordInput, TextInput
from .models import Users


class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password']

        widgets = {
            'username': TextInput(attrs={
                'class': 'form__input',
                'id': 'login',
                'type': 'text',
                'placeholder': 'Логин'
            }),

            'password': PasswordInput(attrs={
                'id': 'password',
                'class': 'form__input',
                'type': 'password',
                'placeholder': 'Пароль'
            })
        }
