from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django import forms

from .models import UserOptions

USER_MODEL = get_user_model()

class UserSignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'autofocus': True,
            'placeholder': 'Username'
        })

        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Password'
        })

        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm password'
        })

        self.fields['first_name'].widget.attrs.update({
            'autofocus': True,
            'placeholder': 'First Name',
        })

        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Last Name'    
        })

        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email (WWU)'    
        })

    def is_valid(self):
        valid = super(UserSignupForm, self).is_valid()
        
        if not valid:
            return valid

        if self.cleaned_data['email'][-8:] == "@wwu.edu":
            return True
        else:
            self.errors["Email"] = "Please enter a valid @wwu.edu email"
            return False
        
        return False

    class Meta:
        model = USER_MODEL
        fields = ('username',
                  'email', 
                  'password1', 
                  'password2',
                  'first_name', 
                  'last_name')

class UserInformationForm(forms.Form):
    employee_types = {
        ("STC", "STC"),
        ("Classroom Services", "Classroom Services")
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

        self.fields['phone_number'].widget.attrs.update({
            'placeholder':'9999999999',
        })

    def clean(self):
        cleaned_data = super(UserOptionsForm, self).clean()
        number = cleaned_data.get('phone_number')
        
        pattern = re.compile('^\d{10}$')
        
        if not pattern.match(number):
            raise forms.ValidationError('Invalid phone_number', code='invalid')
        else:
            return cleaned_data

    class Meta:
        model = UserOptions
        fields = [
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

    class Meat:
        fields = [
            'uuid'
        ]


