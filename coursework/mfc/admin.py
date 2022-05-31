from ast import Pass
from django.contrib import admin
from .models import Users, Passports, Certificates, Departments

# Register your models here.

admin.site.register(Users)
admin.site.register(Passports)
admin.site.register(Certificates)
admin.site.register(Departments)
