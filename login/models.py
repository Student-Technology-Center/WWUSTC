import re
from datetime import datetime

from django import forms
from django.db import models
from django.conf import settings
from django.forms import ModelForm
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
    email = models.BooleanField(default=False)
    texting = models.BooleanField(default=False)
    phone_number = models.CharField(blank=True, max_length=12)

    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    objects = UserOptionsManager()

class UserHiddenAttributes(models.Model):
    reset_key = models.CharField(max_length=7)

    user = models.OneToOneField(settings.AUTH_USER_MODEL)

class UserOptionsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserOptionsForm, self).__init__(*args, **kwargs)

        self.fields['phone_number'].widget.attrs.update({
            'placeholder':'999-999-9999',
        })

    def clean(self):
        cleaned_data = super(UserOptionsForm, self).clean()
        number = cleaned_data.get('phone_number')
        
        pattern = re.compile('^\d{3}[-]\d{3}[-]\d{4}$')
        
        if not pattern.match(number):
            raise forms.ValidationError('Invalid phone_number', code='invalid')
        else:
            return cleaned_data

    class Meta:
        model = UserOptions
        fields = [
            'phone_number',
            'texting',
            'email'
        ]