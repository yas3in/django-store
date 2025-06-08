from django.shortcuts import render
from apps.wallet.models import UserBalance
from django.http import HttpResponse
from apps.wallet.models import Transaction
from django.views.decorators.http import require_http_methods

from django.conf import settings


@require_http_methods(["GET"])
def show_users(request):
    users = settings.AUTH_USER_MODEL.objects.all()
    text = ...
    return HttpResponse(text)
