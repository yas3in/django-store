from datetime import timedelta, timezone
from django.db import models
from random import randint

from apps.accounts.models import CustomUser


class SmsModel(models.Model):
    phone_number = models.ForeignKey(CustomUser, related_name="sms", on_delete=models.CASCADE)
    code = models.CharField()
    is_used = models.BooleanField(default=False)
    is_expired = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return timezone.now() < self.created_at + timedelta(minutes=2)
    
    @classmethod
    def generate_code(cls, phone_humber):
        code = randint(100000, 999999)
        ins = cls.objects.create(
            phone_humber=phone_humber,
            code=code
        )
        return ins

    def verified(self):
        ins = SmsModel.objects.get(id=self.id)
        ins.is_used = True
        ins.save()
