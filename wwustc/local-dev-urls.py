import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'globalvalues'))

from GlobalURLs import GlobalURLs

globalURLs = GlobalURLs()
urlpatterns = globalURLs.urlpatterns

# Add local-dev-urls below
urlpatterns += [
    url(r'^shifts/', include('shiftmanager.urls', namespace='shiftmanager'))
]
