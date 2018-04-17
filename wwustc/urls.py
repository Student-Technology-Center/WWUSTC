import os
import sys

from django.conf import settings
from django.conf.urls import url, include
from wiki.urls import get_pattern as get_wiki_pattern
from django_nyt.urls import get_pattern as get_notify_pattern
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', include('index.urls', namespace="main_page")),
    url(r'^user/', include('login.urls', namespace='login_urls')),
    url(r'^hourmanager/', include('hour_manager.urls')),
    url(r'^notifications/', get_notify_pattern()),
    url(r'^wiki/', get_wiki_pattern()),
    url(r'^lfp/', include('lfp_scheduler.urls')),
    url(r'^evaluations/', include('evaluations.urls')),
    url(r'^bug/', include('bug_tracker.urls', namespace='bugtracker')),
    url(r'^reservations/', include('reservations.urls', namespace='reservations')),
    url(r'^shifts/', include('shiftmanager.urls', namespace='shiftmanager'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
