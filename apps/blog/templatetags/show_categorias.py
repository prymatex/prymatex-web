from django import template
from apps.blog.models import *

def mostrar_categorias():
    categorias = Category.objects.all()
    listado = []
    for c in categorias:
        cant = c.from_category.all().filter(status=2).count()
        if cant:
            listado.append((c, cant))
    
    return {'categorias': listado}


#defino a register
register = template.Library()

#registro el include_tag
register.inclusion_tag('templatetags/mostrar_categorias.html')(mostrar_categorias)
