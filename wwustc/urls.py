import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'globalvalues'))

from GlobalURLs import GlobalURLs

globalURLs = GlobalURLs()
urlpatterns = globalURLs.urlpatterns
#Since this is the prod urls, nothing else should go here
