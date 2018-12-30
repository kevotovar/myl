import string
import random
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from core.models import TimeStampedModel
from .managers import UserManager

USER_TYPE = (
    ('USER', _('user')),
    ('STORE', _('store')),
    ('ADMIN', _('admin')),
)


def ranking_id_generator():
    return ''.join(
        random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6)
    )


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    email = models.EmailField(_('email'), unique=True)
    name = models.CharField(_('name'), max_length=30, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    username = models.CharField(
        _('username'), blank=True, null=True, max_length=60
    )
    type = models.CharField(
        _('type'), choices=USER_TYPE, default=USER_TYPE[0][0], max_length=20
    )
    ranking_id = models.CharField(
        _('id'), max_length=60, default=ranking_id_generator
    )
    points = models.PositiveIntegerField(_('points'), default=0)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    @property
    def avatar(self):
        social_auth_data = self.social_auth.first()
        return 'http://graph.facebook.com/{}/picture?type=large'.format(
            social_auth_data.extra_data.get('id')
        )

    @property
    def full_name(self):
        return self.name or self.username

    @property
    def has_shop(self):
        return bool(self.employee_shop.count())

    @property
    def shop(self):
        return self.employee_shop.first().shop
