from django.conf.urls import url, include

import login.views

urlpatterns = [
    url(r'login/$', login.views.user_login, name='login'),
    url(r'logout/$', login.views.user_logout, name='logout'),
    url(r'profile/$', login.views.profile, name="profile"),
    url(r'register/$', login.views.register),
    url(r'reset/$', login.views.reset_password, name='reset_password')
]

#APIs for lazy adding:
urlpatterns += [
    url(r'api/', include('login.api.api_urls'))
]