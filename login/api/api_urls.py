from django.conf.urls import url

import login.api.api_views as api_views

from .api_views import api_login, register, api_logout, api_confirm_email

urlpatterns = [
    url(r'register/$', register),
    url(r'user_login/$', api_login),
    url(r'user_logout/$', api_logout),
    url(r'confirm_email/(?P<uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', api_confirm_email) 
]