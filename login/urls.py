from django.conf.urls import url, include

import login.views as views

app_name = 'login'

urlpatterns = [
    url(r'^$', views.user_login, name='login'),
    url(r'^profile/',views.profile),
    url(r'^email/$', views.confirm_email, name='base_confirm_email'),
    url(r'^email/(?P<uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', views.confirm_email, name='confirm_email'),
    url(r'^reset/$', views.reset_password, name='reset_request'),
    url(r'^reset/(?P<token>[0-9A-Z]{16})/$', views.reset_password, name='reset_verify')
]

urlpatterns += [
	url(r'api/', include('login.api.api_urls'))
]