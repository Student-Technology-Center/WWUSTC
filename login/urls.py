from django.conf.urls import url, include

import login.views as views

urlpatterns = [
    url(r'^$', views.user_login, name='login'),
    url(r'email/$', views.confirm_email, name='confirm_email'),
    url(r'api/', include('login.api.api_urls'))
]