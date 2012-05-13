# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator, InvalidPage
from django.template import RequestContext
from django.http import HttpResponse, Http404
from django.views.generic.list_detail import object_list

#from tags.models import Tag
'''import datetime'''
from models import Post, Category, EntryTag

ELEMENTOS_POR_PAGINA = 4

def listar_por_categoria(request, slug, page=None):
    categoria = get_object_or_404(Category, slug=slug)
    values = {'titulo':'Categor&iacute;a: %s' % categoria.nombre, "list_categoryes":True,"category":categoria }

    info_dict = {
                 'queryset': Post.objects.all(),
                 
    }


    return object_list(request, 
                       queryset=Post.objects.filter(category=categoria),
                       extra_context = values,
                       paginate_by = ELEMENTOS_POR_PAGINA,
                       page=page)


def  listar_por_tag(request, slug, page=None):
    
    tag = get_object_or_404(EntryTag, slug=slug)
    
    values = {'titulo':'Tag: %s' % tag.nombre, "list_tags":True, "tag":tag}
    
    return object_list(request, 
                       queryset = tag.post_set.all(),
                       extra_context = values,
                       paginate_by = ELEMENTOS_POR_PAGINA,
                       page=page)


# ////////////////////


def leer_post(request, dia, mes, anio, slug ):
    "Esta vista se utiliza para leer un post completo \
    lo que hace es simple obtiene el post y muestra todos \
    sus atributos. \
    Otra cosa que hace es aumentar el contador de lecturas \
    de dicho post llamando al metodo post_leido() de la clase Post \
    "
    ''' primero paso los argumentos dia mes y anio a integer '''
    dia = int(dia); mes=int(mes); anio=int(anio)
    
    ''' luego obtengo el objeto o 404 '''
    post = get_object_or_404(Post, pub_date__day=dia,pub_date__month=mes,pub_date__year=anio,slug=slug)
    
    ''' le decimos al post que fue leido, el aumentara el contador de lecturas '''
    post.post_leido()
    
    try:
        next_post = Post.get_next_by_pub_date(post)
    except Post.DoesNotExist, e:
        next_post = False
    
    try:
        prev_post = Post.get_previous_by_pub_date(post)
    except Post.DoesNotExist, e:
        prev_post = False
        
    values = {
              'post':post,
              'next_post':next_post,
              'prev_post':prev_post,
    }
    
    ''' si estoy aca es porque tengo al post..  lo voy a mostrar '''
    return render_to_response('blog/leer_post.html', values, context_instance = RequestContext(request))

    
  
    