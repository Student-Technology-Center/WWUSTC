from django.db import models
from django.forms import ModelForm
from django.conf import settings

class Issue(models.Model):
    issue = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = [
            'issue'
        ]