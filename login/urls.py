from django.conf.urls import url

import login.views

urlpatterns = [
    url(r'login/$', login.views.user_login),
    url(r'logout/$', login.views.user_logout),
    url(r'register/$', login.views.register)
]