from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    passport_id = models.ForeignKey(
        'mfc.Passports', unique=True, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return (str(self.user_id) + ' ' + str(self.user))


class Passports(models.Model):
    passport_id = models.AutoField('passport_id', primary_key=True)
    first_name = models.CharField('first_name', max_length=30)
    last_name = models.CharField('last_name', max_length=30)
    middle_name = models.CharField('middle_name', max_length=30)
    series = models.IntegerField('series')
    passport_number = models.IntegerField('number')
    branch = models.CharField('branch', max_length=128)
    branch_number = models.IntegerField('branch_number', null=True)
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
        return (str(self.name))


class Articles(models.Model):
    article_id = models.IntegerField('article_id', primary_key=True)
    title = models.CharField('title', max_length=256)
    body = models.TextField('body')
    image_url = models.TextField('image_url')

    def __str__(self):
        return (str(self.article_id) + ' ' + str(self.title))


class Departments(models.Model):
    department_id = models.IntegerField('department_id', primary_key=True)
    name = models.CharField('name', max_length=150)
    city = models.CharField('city', max_length=20)
    street = models.CharField('street', max_length=40)
    house = models.IntegerField('house')
    building = models.IntegerField('building', null=True)

    def __str__(self):
        return (str(self.name))


class Applications(models.Model):

    application_id = models.IntegerField('application_id', primary_key=True)
    certificate = models.ForeignKey(
        'mfc.Certificates', unique=False, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(
        'mfc.Departments', unique=False, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(
        'mfc.Users', unique=False, on_delete=models.CASCADE, null=True, blank=True)
    FULFILLED = 'Выполнено'
    REJECTED = 'Отклонено'
    CANCELED = 'Отменено'
    IN_PROCESS = 'В процессе'
    UNDER_REVIEW = 'Принято к рассмотрению'
    TYPE_CHOICES = [
        (FULFILLED, 'Выполнено'),
        (REJECTED, 'Отклонено'),
        (IN_PROCESS, 'В процессе'),
        (UNDER_REVIEW, 'Принято к рассмотрению'),
        (CANCELED, 'Отменено')
    ]
    state = models.CharField(
        max_length=22,
        choices=TYPE_CHOICES,
        default=UNDER_REVIEW
    )

    def __str__(self):
        return (str(self.application_id) + ' ' + str(self.user) + '-' + str(self.state))
