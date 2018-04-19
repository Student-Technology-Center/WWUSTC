from django.conf.urls import url
from django.views.generic.base import RedirectView

import index.views

app_name = 'index'
favicon_view = RedirectView.as_view(url='/static/favicon.png', permanent=True)


urlpatterns = [
    url(r'^$', index.views.index, name='index'),
    url(r'^favicon\.ico$', favicon_view)
]
