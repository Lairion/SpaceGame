from django.conf.urls import url, include

from .views import (
            register_in_site_post,
            registration,
            login_site,
            character_page,
            login_in_site,
            logout_in_site)
urlpatterns = [
    url(r'^register/$', registration, name="registration" ),
    url(r'^register/post$',register_in_site_post, name="post_registration"),
    url(r'^login/$', login_site, name="login" ),
    url(r'^logout/$',logout_in_site,name="logout"),
    url(r'^login/post$', login_in_site, name="login_post" ),
    url(r'^characters/$', character_page, name="characters" ),
    # url(r'^login/(?P<id>[\w-]+)$', system_view, name="system_map" ),
]