from django.conf.urls import url

import login.views

urlpatterns = [
    url(r'login/$', login.views.user_login, name='login'),
    url(r'logout/$', login.views.user_logout, name='logout'),
    url(r'profile/$', login.views.profile, name="profile"),
    url(r'register/$', login.views.register)
]

#APIs for lazy adding:
urlpatterns += [
    url(r'add_shift/$', login.views.add_shift, name='add_shift')
]