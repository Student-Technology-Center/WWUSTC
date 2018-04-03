from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class StcUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    special_key = forms.CharField(max_length=30, required=True)
    employee_type = forms.ChoiceField(choices=[("STC", "Student Technology Center"), ("CS", "Classroom Services")], required=True)

    def __init__(self, *args, **kwargs):
        super(StcUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'placeholder':'Username',
        })

        self.fields['first_name'].widget.attrs.update({
            'placeholder':'First name',
        })

        self.fields['last_name'].widget.attrs.update({
            'placeholder':'Last name',
        })

        self.fields['email'].widget.attrs.update({
            'placeholder':'stc@wwu.edu',
        })

        self.fields['password1'].widget.attrs.update({
            'placeholder':'Password',
        })

        self.fields['password2'].widget.attrs.update({
            'placeholder':'Confirm password',
        })

        self.fields['special_key'].widget.attrs.update({
            'placeholder':'Normal STC key..',
        })

    def is_valid(self):
        valid = super(StcUserCreationForm, self).is_valid()

        if not valid:
            return valid

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'special_key', 'employee_type')

