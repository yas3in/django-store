from django.shortcuts import render
from wallet.models import UserBalance
from django.http import HttpResponse


def show_users(request):
    users = UserBalance.transactions_count()
    text = ','.join([str(user.balance) for user in UserBalance.transactions_count()])
    return HttpResponse(text)
