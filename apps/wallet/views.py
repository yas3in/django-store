from django.shortcuts import render
from apps.wallet.models import UserBalance
from django.http import HttpResponse
from apps.wallet.models import Transaction
from apps.blog.models import User
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def show_users(request):
    users = User.objects.all()
    text = ...
    return HttpResponse(text)
