# Global settings file, all of these settings here will apply to all instances of the server unless overriden in each file. 

import os

class GlobalSettings():
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.SECRET_KEY = 'v+pm63^+qgh)9qw=&85j_mtoks(bv7l%i=ae!!qo1%4n#4hd41'
        
        self.LOGIN_URL = '/user/login/'
        self.LOGIN_REDIRECT_URL = '/'
        self.ROOT_URLCONF = 'wwustc.urls'
        self.WSGI_APPLICATION = 'wwustc.wsgi.application'
        self.LANGUAGE_CODE = 'en-us'
        self.TIME_ZONE = 'UTC'
        self.STATIC_URL = '/static/'
        self.MEDIA_URL = '/media/'
        
        self.SITE_ID = 1
        
        self.WIKI_ACCOUNT_HANDLING = True
        self.WIKI_ACCOUNT_SIGNUP_ALLOWED = False
        self.SECURE_SSL_REDIRECT = True
        self.USE_I18N = True
        self.USE_L10N = True
        self.USE_TZ = True

        #App specific settings
        
        #shiftmanager
        self.NUM_USERS = 0
        self.CREATING_SHIFTS = False
        self.USER_SHIFT_PLACE = 1

        #index
        self.MOTD = ""
        
        # Any list type of objects should be added onto vs being overriden
        self.ALLOWED_HOSTS = [
            "wwustc.com", 
            "m.wwustc.com", 
        ]

        self.INSTALLED_APPS = [
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
            'bug_tracker.apps.BugTrackerConfig'
        ]

        self.MIDDLEWARE = [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ]
        
        self.AUTHENTICATED_BACKENDS = [
            'django.contrib.auth.backends.ModelBackend'
        ]
        
        self.DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(self.BASE_DIR, 'db.sqlite3'),
            }
        }
        
        self.AUTH_PASSWORD_VALIDATORS = [
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
        
        self.ADMIN_LIST = [
            'brintnc',
            'ConnorHopkins',
            'Slymane',
            'ayalaa2',
        ]
