from django.conf.urls import url

import login.api.api_views as api_views

from .api_views import api_login, register, api_logout

urlpatterns = [
    url(r'register/$', register),
    url(r'user_login/$', api_login),
    url(r'user_logout/$', api_logout)
]