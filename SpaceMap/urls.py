from django.conf.urls import url, include
from .views import (space_view)
urlpatterns = [
    url(r'^space/$', space_view, name="space_map" ),
]