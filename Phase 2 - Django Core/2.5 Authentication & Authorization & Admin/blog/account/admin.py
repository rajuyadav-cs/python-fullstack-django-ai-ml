from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Signupmodel
# Register your models here.

@admin.register(Signupmodel)
class SignupAdminModel(UserAdmin):
    pass