import re
from datetime import datetime

from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class UserOptionsManager(models.Manager):
    def create_options(self, user):
            options = self.create(user)
            options.texting = False
            options.email = False
            options.phone_number = ''
            options.save()
            return options

class UserOptions(models.Model):
    PHONE_CARRIERS = (
        ('at&t','AT&T'),
        ('tmobile','T-Mobile'),
        ('verizon','Verizon'),
        ('sprint','Sprint'),
        ('boost','Boost'),
        ('cricket','Cricket'),
        ('alltell','AllTell'),
        ('metroPCS','MetroPCS'),
        ('projectFi','Project-Fi'),
        ('uscell','US Cellular')
    )

    email = models.BooleanField(default=True)
    texting = models.BooleanField(default=False)
    phone_number = models.CharField(blank=True, max_length=12)
    phone_carrier = models.CharField(blank=True, choices=PHONE_CARRIERS, max_length=64)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    objects = UserOptionsManager()

class UserHiddenAttributes(models.Model):
    reset_key = models.CharField(max_length=7)
    confirmed_account = models.BooleanField(default=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
