# -*- coding: utf-8 -*-

from models import UserProfile
from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','twitter_account')
    
admin.site.register(UserProfile, UserProfileAdmin)
