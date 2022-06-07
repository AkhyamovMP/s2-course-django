from django import forms
from django.forms import ModelForm, PasswordInput, TextInput
from .models import Users


class UserForm(ModelForm):

    newUsername = forms.CharField(
        required=False,
        label='new-username',
        widget=forms.PasswordInput(
            attrs={
                'id': 'new-username',
                'class': 'form__input',
                'type': 'text',
                'placeholder': 'Придумайте логин'
            }
        )
    )

    newPassword = forms.CharField(
        required=False,
        label='new-password',
        widget=forms.PasswordInput(
            attrs={
                'id': 'new-password',
                'class': 'form__input',
                'type': 'password',
                'placeholder': 'Придумайте пароль'
            }
        )
    )

    newPasswordConf = forms.CharField(
        required=False,
        label='new-password-repeat',
        widget=forms.PasswordInput(
            attrs={
                'id': 'new-password-confirm',
                'class': 'form__input',
                'type': 'password',
                'placeholder': 'Повторите пароль'
            }
        )
    )

    class Meta:
        model = Users
        fields = ['username', 'password']

        widgets = {
            'username': TextInput(attrs={
                'class': 'form__input',
                'id': 'login',
                'type': 'text',
                'placeholder': 'Логин',

            }),

            'password': PasswordInput(attrs={
                'id': 'password',
                'class': 'form__input',
                'type': 'password',
                'placeholder': 'Пароль'
            })
        }


