from django.contrib.auth.backends import BaseBackend
from random import randint

from apps.accounts.models import CustomUser


class SmsBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = CustomUser.objects.get(phone_number=username)
        except CustomUser.DoesNotExist:
            return None
        
        if user.check_password(password) and user.is_active:
            return user
        return None


    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
