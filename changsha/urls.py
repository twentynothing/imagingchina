

# Import django modules
from django.conf.urls import patterns, url, include 


urlpatterns = patterns('changsha.views',
    url(r'^$', 'index', name='changsha-index'),
)
