# development.py
from django.core.management.utils import get_random_secret_key
from .base import *

DEBUG = True
SECRET_KEY = get_random_secret_key()
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
# STATIC_ROOT = STATIC_DIR
MEDIA_ROOT = MEDIA_DIR
STATICFILES_DIRS = [
    STATIC_DIR,
    BASE_DIR / "static",
]
