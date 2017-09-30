from django.conf.urls import url, include
from .views import (space_view,system_view,planet_view,city_view)
urlpatterns = [
    url(r'^space/$', space_view, name="space_map" ),
    url(r'^space/(?P<id>[\w-]+)$', system_view, name="system_map" ),
    url(r'^space/system/(?P<id>[\w-]+)$', planet_view, name="planet_view" ),
    url(r'^space/system/planet/(?P<id>[\w-]+)$', city_view, name="city_view" ),
]