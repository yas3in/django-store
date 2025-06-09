from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

from apps.lib.validators import valid_phone_number
from django.utils.translation import gettext_lazy as _


class MyManager(BaseUserManager):


    def create_user(self, phone_number, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not phone_number:
            raise ValueError("Users must have an email address")

        user = self.model(
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            phone_number=phone_number,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    phone_number = models.CharField(_("phone number"), primary_key=True, unique=True, max_length=11, validators=[valid_phone_number])
    first_name = models.CharField(_("first name"), max_length=48, blank=True)
    last_name = models.CharField(_("last name"), max_length=48, blank=True)
    email = models.EmailField(_("email"), blank=True)
    is_admin = models.BooleanField(default=False)
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
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Sms(models.Model):
    phone_number = models.ForeignKey(CustomUser, related_name="sms", on_delete=models.CASCADE, to_field="phone_number")
    code = models.BigIntegerField()
    created_time = models.TimeField(True)
    expire_time = models.TimeField(default=60)


    def check_code(self, request, code, phone_number):
        return True if self.code == code and self.phone_number == phone_number else False

