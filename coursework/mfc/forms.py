from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Articles


class UserRegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
    username = forms.CharField(
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

    password1 = forms.CharField(
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

    password2 = forms.CharField(
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


class UserLoginForm(AuthenticationForm):



    username = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'password',
            'class': 'form__input',
            'placeholder': 'Логин'
        }))
    password = forms.CharField(
        required=False,
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form__input',
            'id': 'login',
            'placeholder': 'Пароль'
        }))


'''
        widgets = {
            
            'username': TextInput(attrs={
                'class': 'form__input',
                'id': 'login',
                'type': 'text',
                'label': 'Имя пользователя',
                'placeholder': 'Логин',

            }),

            'password': PasswordInput(attrs={
                'id': 'password',
                'class': 'form__input',
                'type': 'password',
                'placeholder': 'Пароль'
            })
        }
'''


class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'body', 'image_url']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form__input form__input--role_title',
                'id': 'form-title',
                'type': 'text',
                'placeholder': 'Название статьи',

            }),

            'body': TextInput(attrs={
                'id': 'form-body',
                'class': 'form__input form__input--role_body',
                'type': 'text',
                'placeholder': 'Текст статьи'
            }),


            'image_url': TextInput(attrs={
                'id': 'form-image',
                'class': 'form__input form__input--role_image',
                'type': 'text',
                'placeholder': 'url картинки статьи'
            })
        }


'''
class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['application_date']
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

    date = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control'},
            format='%Y-%m-%dT%H:%M')
    )




        widgets = {
            'title': DateTimeInput(attrs={
                'class': 'form__input',
                'id': 'form-title',
                'type': 'datetime-local',
            })
        }
'''
