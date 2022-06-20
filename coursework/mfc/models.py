from datetime import date
from django.db import models
from sqlalchemy import ForeignKey


class Users(models.Model):
    user_id = models.IntegerField('user_id', primary_key=True)
    username = models.CharField('username', max_length=30, blank=True)
    password = models.CharField('password', max_length=30, blank=True)
    passport_id = models.ForeignKey(
        'mfc.Passports', unique=True, on_delete=models.CASCADE, null=True, blank=True)
    user_type = models.IntegerField('user_type', default=0)

    def __str__(self):
        return (str(self.user_id) + ' ' + str(self.username))


class Passports(models.Model):
    passport_id = models.IntegerField('passport_id', primary_key=True)
    first_name = models.CharField('first_name', max_length=30)
    last_name = models.CharField('last_name', max_length=30)
    middle_name = models.CharField('middle_name', max_length=30)
    series = models.IntegerField('series')
    passport_number = models.IntegerField('number')
    registration = models.TextField('registration')

    def __str__(self):
        return (str(self.passport_id) + ' ' + str(self.first_name) + ' ' + str(self.middle_name) + ' ' + str(self.last_name))


class Certificates(models.Model):
    certificate_id = models.IntegerField('certificate_id', primary_key=True)
    name = models.CharField('name', max_length=128)
    CERTIFICATE = 'CR'
    EXCERPT = 'EX'
    TYPE_CHOICES = [
        (CERTIFICATE, 'Справка'),
        (EXCERPT, 'Выписка')
    ]
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default=CERTIFICATE
    )

    def __str__(self):
        return (str(self.certificate_id) + ' ' + str(self.name))


class Articles(models.Model):
    article_id = models.IntegerField('article_id', primary_key=True)
    author = models.ForeignKey('mfc.Users', on_delete=models.CASCADE)
    title = models.CharField('title', max_length=128)
    body = models.TextField('body')
    image_url = models.TextField('image_url')

    def __str__(self):
        return (str(self.article_id) + ' ' + str(self.title))


class Departments(models.Model):
    departpment_id = models.IntegerField('department_id', primary_key=True)
    name = models.CharField('name', max_length=150)
    city = models.CharField('city', max_length=20)
    street = models.CharField('street', max_length=40)
    house = models.IntegerField('house')
    building = models.IntegerField('building', null=True)

    def __str__(self):
        return (str(self.departpment_id) + ' ' + str(self.name))


class Application(models.Model):
    application_id = models.IntegerField('aoolication_id', primary_key=True)
    certificate_id = models.ForeignKey(
        'mfc.Certificates', unique=False, on_delete=models.CASCADE, null=True, blank=True)
    department_id = models.ForeignKey(
        'mfc.Departments', unique=False, on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey(
        'mfc.Users', unique=False, on_delete=models.CASCADE, null=True, blank=True)
    application_date = models.DateTimeField('application_date')

    def __str__(self):
        return (str(self.application_id))
