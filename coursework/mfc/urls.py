from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginpage, name='loginpage'),
    path('home', views.homepage, name='home'),
    path('certificates', views.certificates, name='certificates'),
    path('search/', views.search, name='search'),
    path('edit-article', views.edit_article, name='edit-article'),
    path('show-certificate/<certificate_id>', views.show_certificate, name='show-certificate')
]
