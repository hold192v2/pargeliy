from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#s^7%e_*2j&d&!-y)6wqc%brbm#buw)qg+zi60+m!-1$q953pa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'home',
        'USER': 'home',
        'PASSWORD': 'govno',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
STATIC_URL = 'static/'

