from django.conf.urls import url
from API.views import (API_resource, API_resource_id)


urlpatterns = [
    url(r'^properties/$', API_resource),
    url(r'^properties/(?P<id>[0-9]+)/$', API_resource_id)
]