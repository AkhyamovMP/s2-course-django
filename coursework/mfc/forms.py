from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Application, Articles, Certificates, Departments, Passports


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


class PassportForm(ModelForm):

    class Meta:
        model = Passports
        fields = ['first_name', 'last_name', 'middle_name',
                  'series', 'passport_number', 'registration', 'branch', 'branch_number']

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'first-name',
            'class': 'form__input form__input--role_name',
            'placeholder': 'Иван'
        }))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'last-name',
            'class': 'form__input form__input--role_name',
            'placeholder': 'Иванов'
        }))
    middle_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'middle-name',
            'class': 'form__input form__input--role_name',
            'placeholder': 'Иванович'
        }))
    series = forms.CharField(
        max_length=4,
        min_length=4,
        widget=forms.TextInput(attrs={
            'id': 'series',
            'class': 'form__input form__input--role_series',
            'placeholder': '1234'

        }))
    series = forms.CharField(
        max_length=4,
        min_length=4,
        widget=forms.TextInput(attrs={
            'pattern': "[0-9]+",
            'id': 'series',
            'class': 'form__input form__input--role_series',
            'placeholder': '1234'
        }))
    passport_number = forms.CharField(
        max_length=6,
        min_length=6,
        widget=forms.TextInput(attrs={
            'pattern': "[0-9]+",
            'id': 'passport-number',
            'class': 'form__input form__input--role_passport-number',
            'placeholder': '123456'
        }))
    branch = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'branch',
            'class': 'form__input form__input--role_branch',
            'placeholder': '123456'
        }))
    branch_number = forms.CharField(
        max_length=6,
        min_length=6,
        widget=forms.TextInput(attrs={
            'pattern': "[0-9]+",
            'id': 'branch-number',
            'class': 'form__input form__input--role_branch-number',
            'placeholder': '123456'
        }))
    registration = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'registration',
            'class': 'form__input form__input--role_registration',
            'placeholder': 'г.Москва, ул.Ленина, д.1, кв.1'
        }))
