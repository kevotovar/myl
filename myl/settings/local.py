from .base import *

DEBUG = True

INSTALLED_APPS += ['debug_toolbar', ]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost'
    }
}
