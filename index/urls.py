from django.conf.urls import url

import index.views

app_name = 'index'

urlpatterns = [
    url(r'^$', index.views.index, name='index')
]