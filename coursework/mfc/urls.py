from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginpage, name='loginpage'),
    path('home', views.homepage, name='home'),
    path('certificates', views.certificates, name='certificates'),
]
