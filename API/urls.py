from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from API.views import API_resource, API_resource_id


urlpatterns = [
    url(r'^properties/$', API_resource),
    url(r'^properties/(?P<id>[0-9]+)/$', API_resource_id),
    path('auth/', obtain_auth_token, name='api_token_auth'),
]