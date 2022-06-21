from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('signin/', views.sign_in, name='sign-in'),
    path('signup/', views.sign_up, name='sign-up'),
    path('logout/', views.user_logout, name='logout'),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('registration/', include('django.contrib.auth.urls')),
    #path('', views.loginpage, name='loginpage'),
    path('', views.homepage, name='home'),
    path('certificates', views.certificates, name='certificates'),
    path('search/', views.search, name='search'),
    path('edit-article', views.edit_article, name='edit-article'),
    path('show-certificate/<certificate_id>',
         views.show_certificate, name='show-certificate'),
    path('article/<article_id>', views.article, name='article')

]
