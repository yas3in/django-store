from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

from apps.lib.validators import valid_phone_number
from django.utils.translation import gettext_lazy as _


class MyManager(BaseUserManager):


    def create_user(self, phone_number, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not phone_number:
            raise ValueError('The Phone number must be set')  # چون phone_number هست، می‌تونی این خط رو حذف یا تغییر بدی
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone_number, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    phone_number = models.CharField(_("phone number"), primary_key=True, unique=True, max_length=11, validators=[valid_phone_number])
    first_name = models.CharField(_("first name"), max_length=48, blank=True)
    last_name = models.CharField(_("last name"), max_length=48, blank=True)
    email = models.EmailField(_("email"), blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    USERNAME_FIELD = 'phone_number'
    
    objects = MyManager()

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True



class Sms(models.Model):
    phone_number = models.ForeignKey(CustomUser, related_name="sms", on_delete=models.CASCADE, to_field="phone_number")
    code = models.BigIntegerField()
    created_time = models.TimeField(True)
    expire_time = models.TimeField(default=60)


    def check_code(self, request, code, phone_number):
        return True if self.code == code and self.phone_number == phone_number else False

