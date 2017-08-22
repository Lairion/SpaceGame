from django.conf.urls import url, include

from .views import (register_in_site_post,registration)
urlpatterns = [
    url(r'^register/$', registration, name="registration" ),
    url(r'^register/post$',register_in_site_post, name="post_registration")
    url(r'^login/$', system_view, name="system_map" ),
    url(r'^Characters/$', system_view, name="system_map" ),
    # url(r'^login/(?P<id>[\w-]+)$', system_view, name="system_map" ),
]