from django.conf.urls import url

import index.views

urlpatterns = [
    url(r'^$', index.views.index, name='index'),
    url(r'issue/$', index.views.issue, name='issue')
]