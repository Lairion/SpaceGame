from django.conf.urls import url, include

from .views import (
            register_in_site_post,
            registration,
            login_site,
            character_page,
            login_in_site,
            logout_in_site,
            character,
            ship_interface,
            catch_defaul_parameters,
            fight,
            attack,
            defence,
            choice_result,
            buy_engine
            )
urlpatterns = [
    url(r'^register/$', registration, name="registration" ),
    url(r'^register/post$',register_in_site_post, name="post_registration"),
    url(r'^login/$', login_site, name="login" ),
    url(r'^logout/$',logout_in_site,name="logout"),
    url(r'^login/post$', login_in_site, name="login_post" ),
    url(r'^characters/$', character_page, name="characters" ),
    url(r'^character/(?P<id>[\w-]+)$', character, name="character" ),
    url(r'^ship/(?P<id>[\w-]+)$', ship_interface, name="ship_interface" ),
    url(r'^prepare/$', catch_defaul_parameters , name="prepare" ),
    url(r'^fight/$', fight, name="fight" ),
    url(r'^attack/$', attack, name="attack" ),
    url(r'^defence/$', defence, name="defence" ),
    url(r'^choice_result/$', choice_result, name="choice_result" ),
    url(r'^buy/engine/$', buy_engine, name="buy_engine" ),
]