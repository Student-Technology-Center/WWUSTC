from django.db import models
from django.conf import settings
from django.forms import ModelForm

class UserOptions(models.Model):
    email = models.BooleanField(default=False)
    texting = models.BooleanField(default=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    def create_options(self, user):
        options = self.create(user)
        options.texting = False
        options.email = False
        options.save()
        return options


class UserOptionsForm(ModelForm):
    class Meta:
        model = UserOptions
        fields = [
            'texting',
            'email'
        ]