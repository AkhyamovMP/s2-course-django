from statistics import mode
from django import forms
from django.forms import DateInput, DateTimeInput, ModelForm, PasswordInput, TextInput
from .models import Articles, Users, Application


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
