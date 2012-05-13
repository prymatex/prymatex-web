from django import template
from apps.blog.models import Post

def show_post(cantidad):
    lista = Post.objects.all()[:cantidad]
    return {'lista': lista}


#defino a register
register = template.Library()

#registro el include_tag
register.inclusion_tag('templatetags/show_posts.html')(show_post)
