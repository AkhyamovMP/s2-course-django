from pyexpat import model
from turtle import title
from django.db import models
from sqlalchemy import ForeignKey, false, true

class Users(models.Model):
    user_id = models.IntegerField('user_id', primary_key=true)
    username = models.CharField('username', max_length=30, blank=True)
    password = models.CharField('password', max_length=30, blank=True)
    passport_id = models.ForeignKey('mfc.Passports', unique=true ,on_delete=models.CASCADE, null=true, blank=true)

    def __str__(self) -> str:
        return super().__str__()


    #def __str__(self):
    #    return (self.user_id, self.username, self.password)


class Passports(models.Model):
    passport_id = models.IntegerField('passport_id', primary_key=true)
    first_name = models.CharField('first_name', max_length=30)
    last_name = models.CharField('last_name', max_length=30)
    middle_name = models.CharField('middle_name', max_length=30)
    series = models.IntegerField('series')
    passport_number = models.IntegerField('number')
    registration = models.TextField('registration')
    
    def __str__(self) -> str:
        return super().__str__()

class Certificates(models.Model):
    certificate_id = models.IntegerField('certificate_id', primary_key=true)
    name = models.CharField('name', max_length=128)

    def __str__(self) -> str:
        return super().__str__()


class Articles(models.Model):
    article_id = models.IntegerField('article_id', primary_key=true)
    title = models.CharField('title', max_length=128)
    body = models.TextField('body')


    def __str__(self) -> str:
        return super().__str__()