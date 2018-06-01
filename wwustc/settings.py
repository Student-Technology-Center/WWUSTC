# Global settings file, all of these settings here will apply to all instances of the server unless overriden in each file. 

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'v+pm63^+qgh)9qw=&85j_mtoks(bv7l%i=ae!!qo1%4n#4hd41'

LOGIN_URL = '/user/'
LOGIN_REDIRECT_URL = '/'
ROOT_URLCONF = 'wwustc.urls'
WSGI_APPLICATION = 'wwustc.wsgi.application'
LANGUAGE_CODE = 'en-us'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

DEBUG = False

EMAIL_HOST_USER = os.environ.get('EMAIL_USERNAME', "")
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD', "")
EMAIL_PORT = 587
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

SITE_ID = 1

WIKI_ACCOUNT_HANDLING = True
WIKI_ACCOUNT_SIGNUP_ALLOWED = False
SECURE_SSL_REDIRECT = True
USE_I18N = True
USE_L10N = True
USE_TZ = True
TIME_ZONE = 'US/Pacific'

ALLOWED_HOSTS = [
    "wwustc.com", 
    "m.wwustc.com", 
]

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
    'bug_tracker.apps.BugTrackerConfig',
    'reservations.apps.ReservationsConfig',
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

AUTHENTICATED_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

STATIC_ROOT = '/var/www/wwustc/static/'
MEDIA_ROOT = '/var/www/wwustc/media/'
