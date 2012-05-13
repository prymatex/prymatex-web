# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list
from models import Post #Import relativo
from views import ELEMENTOS_POR_PAGINA

info_dict = {
    'queryset': Post.objects.all(),
    'paginate_by':ELEMENTOS_POR_PAGINA,
}

urlpatterns=patterns('',
                     (r'^/?$', object_list, dict(info_dict)),
                     (r'^(?P<dia>\d{1,2})/(?P<mes>\d{1,2})/(?P<anio>\d{4})/(?P<slug>[\w\d.-]+)/$', 'apps.blog.views.leer_post'),
                     (r'^tag/(?P<slug>[\w\d.-]+)/$', 'apps.blog.views.listar_por_tag'),
                     (r'^category/(?P<slug>[\w\d.-]+)/$', 'apps.blog.views.listar_por_categoria'),
) 
