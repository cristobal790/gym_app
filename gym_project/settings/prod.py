from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG', True)

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '0.0.0.0').split(',') + os.getenv('DOMAIN', '0.0.0.0').split(',')
CSRF_TRUSTED_ORIGINS = ['http://0.0.0.0', 'http://0.0.0.0:8000', 'http://127.0.0.1:8000', 'http://127.0.0.1']+ALLOWED_HOSTS
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.{}'.format(
            os.getenv('DATABASE_ENGINE', 'postgresql_psycopg2')
        ),
        'NAME': os.getenv('DATABASE_NAME', 'gym_db'),
        'USER': os.getenv('DATABASE_USERNAME', 'gym_app'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'pass'),
        'HOST': os.getenv('DATABASE_HOST', 'postgres'),
        'PORT': os.getenv('DATABASE_PORT', 5432),
        'OPTIONS': json.loads(
            os.getenv('DATABASE_OPTIONS', '{}')
        ),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = '/app/static/'


STATIC_URL = '/static/'
# STATICFILES_DIR = BASE_DIR.parent
STATICFILES_DIRS = [Path(BASE_DIR.parent, 'assets')]