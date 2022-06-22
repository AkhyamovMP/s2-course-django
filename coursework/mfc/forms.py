from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Application, Articles, Departments


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


class ApplicationForm(ModelForm):
    department = forms.ModelMultipleChoiceField(
        queryset=Departments.objects.all(),
        initial=Departments.objects.all()[0],
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control'
            },
        )
    )

    class Meta:
        model = Application
        fields = ['application_date']

