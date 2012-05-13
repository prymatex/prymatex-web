from django import template
from apps.blog.models import EntryTag

def show_all_tags():
    tags = EntryTag.objects.all()
    return {'tags': tags}

#defino a register
register = template.Library()

#registro el include_tag
register.inclusion_tag('templatetags/show_all_tags.html')(show_all_tags)
