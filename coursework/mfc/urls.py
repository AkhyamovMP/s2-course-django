from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('/home', views.homepage, name='home'),
    path('', views.loginpage, name='loginpage')
]
