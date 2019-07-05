from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
from django import forms

import re
from datetime import timedelta

from .models import UserOptions, UserHiddenAttributes
from .helpers import check_password_reset_token

USER_MODEL = get_user_model()

class UserSignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    email = forms.EmailField()

    secret_key = forms.CharField(max_length=12, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username'
        })

        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Password'
        })

        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm password'
        })

        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'First Name',
        })

        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Last Name'    
        })

        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email (WWU)'    
        })

        self.fields['secret_key'].widget.attrs.update({
            'placeholder': 'Ask for the secret key'    
        })

    def is_valid(self):
        valid = super(UserSignupForm, self).is_valid()
        
        if not valid:
            return valid

        if not self.cleaned_data['email'][-8:] == "@wwu.edu":
            self.errors["Email"] = "Please enter a valid @wwu.edu email"
            return False

        # REGISTRATION_SECRET is a envrionment var that is gathered by settings.py
        # This is used to prevent random patrons from accidently registering for
        # the website
        print(settings.REGISTRATION_SECRET)
        if not settings.REGISTRATION_SECRET:
            self.errors["Secret"] = "Registration secret value not setup"

        elif self.cleaned_data['secret_key'] == settings.REGISTRATION_SECRET:
            return True
        else:
            self.errors["Secret"] = "Invalid secret key!"

        return False

    class Meta:
        model = USER_MODEL
        fields = [
            'username',
            'email', 
            'password1', 
            'password2',
            'first_name', 
            'last_name'
        ]   

class UserInformationForm(forms.Form):
    employee_types = {
        ("STC", "STC")
    }

    employee_type = forms.ChoiceField(choices=employee_types)

    def __init__(self, *args, **kwargs):
        super(UserInformationForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        valid = super(UserInformationForm, self).is_valid()

        if not valid:
            return valid

        return valid

    class Meta:
        fields = [
            "key",
            "employee_type"
        ]

class UserOptionsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserOptionsForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = False

        self.fields['phone_number'].widget.attrs.update({
            'placeholder':'4253233242',
        })

        self.fields['shift_name'].widget.attrs.update({
            'placeholder': 'Shift name'
        })

    def clean(self):
        cleaned_data = super(UserOptionsForm, self).clean()
        number = cleaned_data.get('phone_number')

        pattern = re.compile('\d{3}-?\d{3}-?\d{4}')
        
        if not pattern.match(number) and number != "":
            raise forms.ValidationError('Invalid phone number', code='invalid')
        else:
            return cleaned_data

    class Meta:
        model = UserOptions
        fields = [
            'shift_name',
            'phone_number',
            'phone_carrier',
            'texting',
            'email'
        ]

class UserLoginForm(forms.Form):
    login = forms.CharField(max_length=32)
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.fields['login'].widget.attrs.update({
            'autofocus': True,
            'placeholder':'Username',
        })

        self.fields['password'].widget.attrs.update({
            'placeholder':'Password',
        })

    def is_valid(self):
        valid = super(UserLoginForm, self).is_valid()

        if not valid:
            return valid

        return valid

    class Meta:
        fields = [
            'username',
            'password'
        ]

class EmailConfirmationForm(forms.Form):
    uuid = forms.UUIDField()

    def __init__(self, *args, **kwargs):
        super(EmailConfirmationForm, self).__init__(*args, **kwargs)

        self.fields['uuid'].widget.attrs.update({
            'placeholder': 'Confirmation key'    
        })

    def is_valid(self):
        valid = super(EmailConfirmationForm, self).is_valid()

        if not valid:
            return valid

        return valid

    class Meta:
        fields = [
            'uuid'
        ]

class PasswordResetRequest(forms.Form):
    username = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(PasswordResetRequest, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Your username'    
        })

    def is_valid(self):
        valid = super(PasswordResetRequest, self).is_valid()
        user = None
        try:
            user = USER_MODEL.objects.get(username=self.cleaned_data.get('username'))
        except User.DoesNotExist:
            pass

        if not valid or not user:
            return False
        
        return True

    class Meta:
        fields = [
            'username'
        ]

class PasswordResetVerify(forms.Form):
    key = forms.CharField(max_length=16)

    def __init__(self, *args, **kwargs):
        super(PasswordResetVerify, self).__init__(*args, **kwargs)
    
        self.fields['key'].widget.attrs.update({
            'placeholder': 'Key sent to email'    
        })

    def is_valid(self):
        valid = super(PasswordResetVerify, self).is_valid()

        if not valid:
            return False    

        return check_password_reset_token(self.cleaned_data.get('key'))

    class Meta:
        fields = [
            'key'
        ]

class NewPasswordForm(forms.Form):
    new_pass = forms.CharField(min_length=8, widget=forms.PasswordInput, label="New password")
    verify_pass = forms.CharField(min_length=8, widget=forms.PasswordInput, label="Confirm")
    token = forms.CharField(max_length=16, widget=forms.HiddenInput, label="Token")

    def __init__(self, *args, **kwargs):
        super(NewPasswordForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        valid = super(NewPasswordForm, self).is_valid()

        if not valid:
            return False

        matching_passwords = self.cleaned_data.get('new_pass') == self.cleaned_data.get('verify_pass')

        return check_password_reset_token(self.cleaned_data.get('token')) and matching_passwords
    
    class Meta:
        fields = [
            'new_pass',
            'verify_pass',
            'token'
    ]
