from django.conf.urls import url

import login.api.api_views as api_views

from .api_views import *

urlpatterns = [
    url(r'register/$', register),
    url(r'user_login/$', api_login),
    url(r'user_logout/$', api_logout),
    url(r'send_confirmation_email/$', send_email),
    url(r'reset_request/$', reset_request),
    url(r'reset_verify/$', reset_verify),
    url(r'set_password/$', set_password),
]