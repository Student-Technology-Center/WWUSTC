from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from wiki.urls import get_pattern as get_wiki_pattern
from django_nyt.urls import get_pattern as get_nyt_pattern

# Global URLs file, all of the urls here will apply to all instances of the server unless overriden.
# Practically prod
#Index redirect
GLOBAL_urlpatterns = [
    url(r'^', include('index.urls', namespace="main_page"))
]

#Login redirect
GLOBAL_urlpatterns += [
    url(r'^user/', include('login.urls', namespace='login_urls'))
]

#Hour manager redirect
GLOBAL_urlpatterns += [
    url(r'^hourmanager/', include('hour_manager.urls'))
]

#Wiki redirect
GLOBAL_urlpatterns += [
    url(r'^notifications/', get_nyt_pattern()),
    url(r'^wiki/', get_wiki_pattern())
]

#LFP redirect
GLOBAL_urlpatterns += [
    url(r'^lfp/', include('lfp_scheduler.urls')),
]

#Evaluation page redirect
GLOBAL_urlpatterns += [
    url(r'^evaluations/', include('evaluations.urls'))
]

#Bug tracker redirect
GLOBAL_urlpatterns += [
    url(r'^bug/', include('bug_tracker.urls', namespace='bugtracker'))
]

GLOBAL_urlpatterns += [
	url(r'^reservations/', include('reservations.urls', namespace='reservations'))
]

GLOBAL_urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
GLOBAL_urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)