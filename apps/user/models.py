import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework.exceptions import ValidationError


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValidationError(_("Valid Email must be provided"))
        if isinstance(email, str):
            email = email.lower()
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, first_name, last_name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(verbose_name=_("UUID"), primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30, verbose_name=_("First name"), db_index=True)
    last_name = models.CharField(max_length=30, verbose_name=_("Last name"), db_index=True)
    email = models.EmailField(unique=True, verbose_name=_("Email"), db_index=True, editable=False)
    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))
    is_staff = models.BooleanField(default=False, verbose_name=_("Is Staff"))
    created_at = models.DateTimeField(verbose_name=_("Created at"), auto_now_add=True, auto_now=False, editable=False)
    updated_at = models.DateTimeField(
        verbose_name=_("Updated at"), auto_now_add=False, auto_now=True, null=True, blank=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name", "last_name"
    ]
