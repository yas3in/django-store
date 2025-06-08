from django.contrib import admin
from django.contrib.admin import register

from .models import CustomUser

@register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["phone_number", "first_name", "last_name"]