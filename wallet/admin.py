from django.contrib import admin
from django.contrib.admin import register
from wallet.models import Transaction, UserBalance


@register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("user", "transaction_type", "amount", "created_time")



@register(UserBalance)
class UserBalanceAdmin(admin.ModelAdmin):
    list_display = ("user", "balance", "created_time")
