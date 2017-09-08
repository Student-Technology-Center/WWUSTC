from django.conf.urls import url

import login.api.api_views as api_views

urlpatterns = [
    url(r'send_user_email/$', api_views.send_user_email)
]