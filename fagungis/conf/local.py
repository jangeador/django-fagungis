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

ALLOWED_HOSTS = []

SECRET_KEY = '!$6$*2no&ylbdo#9hzf=y^l%gz9n5cgi8hl7gn1!y5b)-i^ksz'

INTERNAL_IPS = ('127.0.0.1')

