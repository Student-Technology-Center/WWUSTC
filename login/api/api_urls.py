from django.conf.urls import url

from login.api.api_views import get_user_shifts, add_shift

urlpatterns = [
    url(r'add_shift/$', add_shift, name='add_shift'),
    url(r'user_shifts/$', get_user_shifts, name='get_user_shifts')
]