# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
import urllib, hashlib


class UserProfile(models.Model):
    
    user = models.ForeignKey(User, unique=True)

    twitter_account = models.CharField(max_length=100, blank=True)
    blog_url = models.URLField(verify_exists=True, blank=True)
    feed_url = models.URLField(verify_exists=True, blank=True)
    use_gravatar = models.BooleanField(default = True)
    
    
    def get_grevatar_src(self):
        size = 80
        rating = 'g'
        default = ''
        gravatar_base = 'https://secure.gravatar.com/avatar'
        url = "%s/%s.jpg?%s" % (gravatar_base,
                                hashlib.md5(self.user.email).hexdigest(),
                                urllib.urlencode({
                                                  'size': str(size),
                                                  'rating': rating,
                                                  'default': default,
                                }))
        return url

    @classmethod
    def getUserProfile(cls, user):
        try:
            profile = user.get_profile()
        except:
            profile = UserProfile()
            profile.user = user
            profile.save()
        return profile
            
        
    
