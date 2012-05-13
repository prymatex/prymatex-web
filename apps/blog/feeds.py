# -*- coding: utf-8 -*-

from django.contrib.syndication.feeds import Feed
from apps.blog.models import Post
from django.utils import feedgenerator

class LatestEntries(Feed):
    title = "Prymatex Blog"
    link = "/blog/"
    description = "Latest Blog Entries"
    feed_type = feedgenerator.Rss201rev2Feed

    title_template = 'feeds/title.html'
    description_template = 'feeds/ultimosposts.html'

    def items(self):
        return Post.objects.order_by('-pub_date')[:10]

