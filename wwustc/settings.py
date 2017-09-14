"""
Django settings for wwustc project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v+pm63^+qgh)9qw=&85j_mtoks(bv7l%i=ae!!qo1%4n#4hd41'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ["wwustc.com", "dev.wwustc.com", "m.wwustc.com", "mdev.wwustc.com"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django_nyt',
    'mptt',
    'sekizai',
    'sorl.thumbnail',
    'wiki',
    'wiki.plugins.attachments',
    'wiki.plugins.notifications',
    'wiki.plugins.images',
    'wiki.plugins.macros',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hour_manager.apps.HourManagerConfig',
    'lfp_scheduler.apps.LfpConfig',
    'index.apps.IndexConfig',
    'evaluations.apps.EvaluationsConfig',
    'login.apps.LoginConfig',
    'shiftmanager.apps.ShiftmanagerConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

LOGIN_URL = '/user/login/'
LOGIN_REDIRECT_URL = '/'

AUTHENTICATED_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend'
]

ROOT_URLCONF = 'wwustc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
            ],
        },
    },
]

WSGI_APPLICATION = 'wwustc.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
<<<<<<< HEAD
STATIC_ROOT = '/var/www/wwustc/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/www/wwustc/media/'
=======
<<<<<<< HEAD
STATIC_ROOT = '/var/www/dev/wwustc/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/www/dev/wwustc/media/'
=======
STATIC_ROOT = '/var/www/wwustc/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/www/wwustc/media/'
>>>>>>> Add a more hard configured path to media
>>>>>>> Add a more hard configured path to media

SITE_ID = 1

WIKI_ACCOUNT_HANDLING = True
WIKI_ACCOUNT_SIGNUP_ALLOWED = False

SECURE_SSL_REDIRECT = True

#App specific settings

#user specific
ADMIN_LIST = [
    'brintnc',
]

#shiftmanager
NUM_USERS = 0
CREATING_SHIFTS = False
USER_SHIFT_PLACE = 1

#index
MOTD = ""