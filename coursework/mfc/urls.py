from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('signin/', views.sign_in, name='sign-in'),
    path('signup/', views.sign_up, name='sign-up'),
    path('logout/', views.user_logout, name='logout'),
    path('add-passport', views.add_passport, name='add-passport'),
    path('show-passport', views.show_passport, name='show-passport'),
    path('', views.homepage, name='home'),
    path('certificates', views.certificates, name='certificates'),
    path('search/', views.search, name='search'),
    path('edit-article', views.edit_article, name='edit-article'),
    path('add-certificate/<certificate_id>',
         views.add_certificate, name='add-certificate'),
    path('article/<article_id>', views.article, name='article'),
    path('all-services', views.all_services, name='all-services'),
    path('in-process', views.in_process, name='in-process')

]
