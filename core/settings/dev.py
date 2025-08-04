from .base import *
from decouple import config

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+2!w@ri+^oz4@82_aa%&6$xw(sgf25t@n$(g3v7ogyb-@qk+j4'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('django_db_name_dev'),
        'USER': config('django_db_user_dev'),
        'PASSWORD': config('django_db_password_dev'),
        'HOST': config('django_db_host_dev'),
        'PORT': config('django_db_port_dev'),
    }
}