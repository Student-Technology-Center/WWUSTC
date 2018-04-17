import uuid

from django.db import models
from django.conf import settings

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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class UserHiddenAttributes(models.Model):
    reset_key = models.CharField(max_length=7)
    confirmation_key = models.UUIDField(default=uuid.uuid4, editable=False)
    confirmed_account = models.BooleanField(default=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
