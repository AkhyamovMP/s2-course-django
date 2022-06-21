from django.contrib import admin
from .models import Articles, Users, Passports, Certificates, Departments, Application

# Register your models here.

admin.site.register(Users)
admin.site.register(Passports)
admin.site.register(Certificates)
admin.site.register(Departments)
admin.site.register(Articles)
admin.site.register(Application)
