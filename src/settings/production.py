# production.py
from django.core.management.utils import get_random_secret_key
from .base import *
import environ

env = environ.Env()
env.read_env()


DEBUG = True
SECRET_KEY = get_random_secret_key()
ALLOWED_HOSTS = ['propfeed.nord-streams.com', '127.0.0.1', '*']

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASS"),
        'HOST': os.environ.get("DB_HOST"),
        'PORT': 3306,
    }
}

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = STATIC_DIR
MEDIA_ROOT = MEDIA_DIR


