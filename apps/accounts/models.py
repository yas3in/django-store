from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser

from apps.lib.validators import valid_phone_number

from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractBaseUser):
    phone_number = models.CharField(_("phone number"), primary_key=True, unique=True, max_length=11, validators=[valid_phone_number])
    first_name = models.CharField(_("first name"), max_length=48, blank=True)
    last_name = models.CharField(_("last name"), max_length=48, blank=True)
    email = models.EmailField(_("email"), blank=True)

    USERNAME_FIELD = 'phone_number'


class Sms(models.Model):
    phone_number = models.ForeignKey(CustomUser, related_name="sms", on_delete=models.CASCADE, to_field="phone_number")
    code = models.BigIntegerField()
    created_time = models.TimeField(True)
    expire_time = models.TimeField(default=60)


    def check_code(self, request, code, phone_number):
        return True if self.code == code and self.phone_number == phone_number else False

