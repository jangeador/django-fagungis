from . import base

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '%(psql_db)s',
        'USER': '%(psql_user)s',
        'PASSWORD': '%(psql_password)s',
        'HOST': 'localhost',
        'PORT': '',
    },
}

# Recipients of traceback emails and other notifications.
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

DEBUG = TEMPLATE_DEBUG = True

DEV = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = 'CHANGE_THIS-1234554321'

INTERNAL_IPS = ('127.0.0.1')

