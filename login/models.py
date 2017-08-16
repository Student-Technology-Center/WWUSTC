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

class Shift(models.Model):
    DAYS_OF_WEEK = [
        ('Mon','Monday'),
        ('Tue','Tuesday'),
        ('Wed','Wednesday'),
        ('Thu','Thursday'),
        ('Fri','Friday'),
        ('Sat','Saturday'),
        ('Sun','Sunday'),
    ]

    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.CharField(max_length=3, choices=DAYS_OF_WEEK, default='Mon')

    user = models.ForeignKey(settings.AUTH_USER_MODEL)

class ShiftForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ShiftForm, self).__init__(*args, **kwargs)

        self.fields['start_time'].widget.attrs.update({
            'placeholder':'12:00',
        })

        self.fields['end_time'].widget.attrs.update({
            'placeholder':'14:00',
        })

    def clean(self):
        cleaned_data = super(ShiftForm, self).clean()
        day = cleaned_data.get('day_of_week')
        start = cleaned_data.get('start_time')
        end = cleaned_data.get('end_time')

        if start >= end:
            raise forms.ValidationError('Start time must be after end time.', code='start')

        if not day:
            raise forms.ValidationError('Please enter a day.')
        
        normal_hours = ['Mon', 'Tue', 'Wed', 'Thu']

        if day in normal_hours:
            print("From {} to {}".format(start, end))

        if day == 'Fri':
            print("From {} to {}".format(start, end))

        if day == 'Sat':
            print("From {} to {}".format(start, end))

        if day == 'Sun':
            print("From {} to {}".format(start, end))

    class Meta:
        model = Shift
        fields = [
            'start_time',
            'end_time',
            'day_of_week'
        ]