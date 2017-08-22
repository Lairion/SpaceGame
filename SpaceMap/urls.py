from django.conf.urls import url, include
from .views import (space_view,system_view)
urlpatterns = [
    url(r'^space/$', space_view, name="space_map" ),
    url(r'^space/(?P<id>[\w-]+)$', system_view, name="system_map" ),
]