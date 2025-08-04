from .base import *
import decouple

DEBUG = False
SECRET_KEY = 'phuss-+2!w@ri+^oz4@82_aa%&6$xw(sgf25t@n$(g3v7ogyb-@qk+j4'

ALLOWED_HOSTS = ['connectappnriit.com']

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': decouple.config('django_db_name_prod'),
        'USER': decouple.config('django_db_user_prod'),
        'PASSWORD': decouple.config('django_db_password_prod'),
        'HOST': decouple.config('django_db_host_prod'),
        'PORT': decouple.config('django_db_port_prod'),
    }
}
