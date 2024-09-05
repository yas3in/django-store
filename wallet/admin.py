from django.contrib import admin
from django.contrib.admin import register
from wallet.models import Transaction, UserBalance


@register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass



@register(UserBalance)
class UserBalanceAdmin(admin.ModelAdmin):
    pass
