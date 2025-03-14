from django.contrib import admin
from .models import BasketLine, Basket


class BasketLineInline(admin.TabularInline):
    model = BasketLine
    
@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ["user", "created_time"]
    inlines = [BasketLineInline]    

