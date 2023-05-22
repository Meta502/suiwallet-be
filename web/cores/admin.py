from django.contrib import admin

from cores.models import SuiwalletUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(SuiwalletUser, UserAdmin)
