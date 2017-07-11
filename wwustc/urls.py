"""wwustc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from wiki.urls import get_pattern as get_wiki_pattern
from django_nyt.urls import get_pattern as get_nyt_pattern

#Index redirect
urlpatterns = [
    url(r'^', include('index.urls', namespace="main_page"))
]

urlpatterns += [
    url(r'^user/', include('login.urls'))
]

#Hour manager redirects
urlpatterns += [
    url(r'^hourmanager/', include('hour_manager.urls'))
]

#LFP redirects
urlpatterns += [
    url(r'^lfp/', include('lfp_scheduler.urls'))
]

urlpatterns += [
    url(r'^notifications/', get_nyt_pattern()),
    url(r'^wiki/', get_wiki_pattern())
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
