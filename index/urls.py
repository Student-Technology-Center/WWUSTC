from django.conf.urls import url

import index.views

urlpatterns = [
    url(r'^$', index.views.index)
]