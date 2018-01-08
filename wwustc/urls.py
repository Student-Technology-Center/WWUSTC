import os
import sys
from django.conf.urls import url
from django.conf.urls import include

sys.path.append(os.path.join(os.path.dirname(__file__), 'globalvalues'))
from GlobalURLs import GLOBAL_urlpatterns

urlpatterns = GLOBAL_urlpatterns
#Shift manager redirect
urlpatterns += [
    url(r'^shifts/', include('shiftmanager.urls', namespace='shiftmanager'))
]
