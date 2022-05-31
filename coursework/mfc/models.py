from pyexpat import model
from turtle import title
import turtle
from django.db import models
from sqlalchemy import ForeignKey


class Users(models.Model):
    user_id = models.IntegerField('user_id', primary_key=True)
    username = models.CharField('username', max_length=30, blank=True)
    password = models.CharField('password', max_length=30, blank=True)
    passport_id = models.ForeignKey(
        'mfc.Passports', unique=True, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return super().__str__()

    # def __str__(self):
    #    return (self.user_id, self.username, self.password)


class Passports(models.Model):
    passport_id = models.IntegerField('passport_id', primary_key=True)
    first_name = models.CharField('first_name', max_length=30)
    last_name = models.CharField('last_name', max_length=30)
    middle_name = models.CharField('middle_name', max_length=30)
    series = models.IntegerField('series')
    passport_number = models.IntegerField('number')
    registration = models.TextField('registration')

    def __str__(self) -> str:
        return super().__str__()


class Certificates(models.Model):
    certificate_id = models.IntegerField('certificate_id', primary_key=True)
    name = models.CharField('name', max_length=128)

    def __str__(self) -> str:
        return super().__str__()


class Articles(models.Model):
    article_id = models.IntegerField('article_id', primary_key=True)
    title = models.CharField('title', max_length=128)
    body = models.TextField('body')

    def __str__(self) -> str:
        return super().__str__()


class Departments(models.Model):
    departpment_id = models.IntegerField('department_id', primary_key=True)
    name = models.CharField('name', max_length=150)
    city = models.CharField('city', max_length=20)
    street = models.CharField('street', max_length=40)
    house = models.IntegerField('house')
    building = models.IntegerField('building', null=True)
