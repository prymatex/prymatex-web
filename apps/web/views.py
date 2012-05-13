# -*- coding: utf-8 -*-
"""
THE PRYMATEX WEB PAGE
"""

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, Http404


def home(request):
    """
    The Home Page
    """
    values= {'title':'Home','menu':'home'}
    context_instance = RequestContext(request)
    return render_to_response('web/home.html',values, context_instance)



def media(request):
    """
    The Media Page
    """
    values= {'title':'Media','menu':'media'}
    context_instance = RequestContext(request)
    return render_to_response('web/media.html',values, context_instance)


def docs(request):
    """
    The Docs Page
    """
    values= {'title':'Docs','menu':'docs'}
    context_instance = RequestContext(request)
    return render_to_response('web/docs.html',values, context_instance)


def about(request):
    """
    The About Page
    """
    values= {'title':'About','menu':'about'}
    context_instance = RequestContext(request)
    return render_to_response('web/about.html',values, context_instance)




 
