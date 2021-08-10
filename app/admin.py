from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserModel

@admin.register(UserModel)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'gender', 'date_created']