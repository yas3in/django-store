from django.contrib.auth import authenticate
from django.http import JsonResponse
from apps.sendcode.models import SmsModel


def send_code(request):
    code = SmsModel.generate_code(request.POST.get("phone_number"))
    return JsonResponse({"code": code})

def login(request):
    pass