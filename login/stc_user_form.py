from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class StcUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    key = forms.CharField(max_length=64, required=False, help_text='If you are unsure what this is, ignore it.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'key')

