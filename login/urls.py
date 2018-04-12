from django.conf.urls import url, include

import login.views

urlpatterns = [
    url(r'^$', login.views.user_login, name='login'),
    url(r'api/', include('login.api.api_urls'))
]