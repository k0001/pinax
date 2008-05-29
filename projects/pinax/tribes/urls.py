from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'tribes.views.tribes', name="tribes_list"),
    url(r'^(\w+)/$', 'tribes.views.tribe', name="tribe_detail"),
    url(r'^topic/(\d+)/$', 'tribes.views.topic', name="tribe_topic"),
)