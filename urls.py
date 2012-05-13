# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from apps.blog.feeds import LatestEntries

feeds = {
    'posts': LatestEntries,
}

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'apps.web.views.home', name='home'),
    url(r'^blog/', include('apps.blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),

)

