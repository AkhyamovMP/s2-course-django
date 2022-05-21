from pyexpat import model
from django.db import models
from numpy import number
from sqlalchemy import ForeignKey, true

class Users(models.Model):
    user_id = models.IntegerField('user_id', primary_key=true)
    username = models.CharField('username', max_length=30)
    password = models.CharField('password', max_length=30)
    # passport_id = models.ForeignKey('Passport', unique=true ,on_delete=models.CASCADE)

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