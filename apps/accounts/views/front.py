from django.contrib.auth import authenticate
from apps.accounts.models import Sms


def login_with_number(request):
    phone_number = request.kgargs.post("phone_Number")
    code = "44444"

    instance = Sms.objects.create(
        
    )

