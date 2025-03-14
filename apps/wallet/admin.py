from django.contrib import admin
from django.contrib.admin import register
from .models import Transaction, UserBalance


@register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    delete_confirmation_template = True
    list_display = ("user", "transaction_type", "amount", "created_time")



@register(UserBalance)
class UserBalanceAdmin(admin.ModelAdmin):
    list_display = ("user", "balance", "created_time")
