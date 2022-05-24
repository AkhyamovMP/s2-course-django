from ast import Pass
from django.contrib import admin
from .models import Users
from .models import Passports
from .models import Certificates
# Register your models here.

admin.site.register(Users)
admin.site.register(Passports)
admin.site.register(Certificates)
