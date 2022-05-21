from ast import Pass
from django.contrib import admin
from .models import Users
from .models import Passports
# Register your models here.

admin.site.register(Users)
admin.site.register(Passports)
