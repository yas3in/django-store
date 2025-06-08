from django.contrib.auth.backends import BaseBackend
from random import randint


class SmsBackend(BaseBackend):
    def send_sms(self):
        pass

    def authenticate(self, request, phone, password):
        pass