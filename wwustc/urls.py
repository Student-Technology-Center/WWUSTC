from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from wiki.urls import get_pattern as get_wiki_pattern
from django_nyt.urls import get_pattern as get_nyt_pattern

import django_cas_ng.views

#Index redirect
urlpatterns = [
    url(r'^', include('index.urls', namespace="main_page"))
]

urlpatterns += [
    url(r'^user/', include('login.urls', namespace='login_urls'))
]

#Hour manager redirects
urlpatterns += [
    url(r'^hourmanager/', include('hour_manager.urls'))
]

urlpatterns += [
    url(r'^notifications/', get_nyt_pattern()),
    url(r'^wiki/', get_wiki_pattern())
]

urlpatterns += [
    url(r'^lfp/', include('lfp_scheduler.urls')),
]

urlpatterns += [
    url(r'^accounts/login$', django_cas_ng.views.login, name='cas_ng_login'),
    url(r'^accounts/logout$', django_cas_ng.views.logout, name='cas_ng_logout'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
