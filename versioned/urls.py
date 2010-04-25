from django.conf.urls.defaults import *

urlpatterns = patterns('testing.versioned.views',
    url(r'^item/(?P<item_id>[0-9]+)/?$', 'item', name="item"),
)