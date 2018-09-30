from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from core.models import TimeStampedModel
from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    email = models.EmailField(_('email'), unique=True)
    name = models.CharField(_('name'), max_length=30, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    username = models.CharField(
        _('username'), blank=True, null=True, max_length=60
    )

    USERNAME_FIELD = 'email'

    objects = UserManager()
