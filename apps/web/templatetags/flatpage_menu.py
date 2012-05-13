from django.template import Library, Node
from django.contrib.flatpages.models import FlatPage
register = Library()

def flatpage_menu():
    pages = FlatPage.objects.all()
    menu = ""
    for i in range(len(pages)):
        menu += '<li>'+'<a href="'+pages[i].url+'" title="'+pages[i].title+'">'+pages[i].title+'</a></li>'
    return menu 

register.simple_tag(flatpage_menu)