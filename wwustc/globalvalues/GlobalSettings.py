# Global settings file, all of these settings here will apply to all instances of the server unless overriden in each file. 

import os

GLOBAL_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLOBAL_SECRET_KEY = 'v+pm63^+qgh)9qw=&85j_mtoks(bv7l%i=ae!!qo1%4n#4hd41'

GLOBAL_LOGIN_URL = '/user/'
GLOBAL_LOGIN_REDIRECT_URL = '/'
GLOBAL_ROOT_URLCONF = 'wwustc.urls'
GLOBAL_WSGI_APPLICATION = 'wwustc.wsgi.application'
GLOBAL_LANGUAGE_CODE = 'en-us'
GLOBAL_TIME_ZONE = 'UTC'
GLOBAL_STATIC_URL = '/static/'
GLOBAL_MEDIA_URL = '/media/'

GLOBAL_SITE_ID = 1

GLOBAL_WIKI_ACCOUNT_HANDLING = True
GLOBAL_WIKI_ACCOUNT_SIGNUP_ALLOWED = False
GLOBAL_SECURE_SSL_REDIRECT = True
GLOBAL_USE_I18N = True
GLOBAL_USE_L10N = True
GLOBAL_USE_TZ = True

#App specific settings

#shiftmanager
GLOBAL_NUM_USERS = 0
GLOBAL_CREATING_SHIFTS = False
GLOBAL_USER_SHIFT_PLACE = 1

#index
GLOBAL_MOTD = ""

# Any list type of objects should be added onto vs being overriden
GLOBAL_ALLOWED_HOSTS = [
    "wwustc.com", 
    "m.wwustc.com", 
]

GLOBAL_INSTALLED_APPS = [
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
    'reservations.apps.ReservationsConfig'
]

GLOBAL_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

GLOBAL_AUTHENTICATED_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend'
]

GLOBAL_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(GLOBAL_BASE_DIR, 'db.sqlite3'),
    }
}

GLOBAL_AUTH_PASSWORD_VALIDATORS = [
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

GLOBAL_ADMIN_LIST = [
    'brintnc',
    'ConnorHopkins',
    'Slymane',
    'ayalaa2',
]
