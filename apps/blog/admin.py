from models import Post, Category, EntryTag
from django.contrib import admin
from django.conf import settings

#---------------------------------------------------------------
class EntryTagAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    prepopulated_fields = {'slug': ('nombre',)}
    
admin.site.register(EntryTag, EntryTagAdmin)



#---------------------------------------------------------------
from django import forms
class PostAdminForm(forms.ModelForm):
 
    def __init__(self, *args, **kwargs):
        super(PostAdminForm, self).__init__(*args, **kwargs)
        self.tags = forms.ModelMultipleChoiceField(queryset=EntryTag.objects.all(),
                                                   widget = admin.widgets.FilteredSelectMultiple('tags', is_stacked=True),
                                                   required = False,)
        #wtf = Category.objects.filter(pk=self.instance.cat_id);
        #w = self.fields['categories'].widget
        #choices = []
        #for choice in wtf:
        #    choices.append((choice.id, choice.name))
        #w.choices = choices


class PostAdmin(admin.ModelAdmin):
    list_display        = ('titulo', 'autor', 'pub_date', 'lecturas','votos_positivos','votos_negativos','category',)
    list_filter         = ('pub_date', 'status',)
    search_fields       = ('titulo', 'descripcion', 'cuerpo')
    prepopulated_fields = {'slug': ('titulo',)}
    fieldsets = (
        ('Titulo', {'fields': ('titulo',)}),
        ('Texto', {'fields':('texto',)}),
        ('Categor&iacute;as y Tags', {'fields':(('category','tags',),)}),   
        ('Opciones',{'fields':(('slug','allow_comments','status'),)}),
    )
    form = PostAdminForm
    class Media:
        css = {
            "all": ("/site_media/css/myadmin.css",)
        }
        js = ('/site_media/js/tinymce/jscripts/tiny_mce/tiny_mce.js','/site_media/js/prymatex_admin.js',)
    
    def save_model(self, request, obj, form, change):
        instance = form.save(commit = False)
        instance.autor = request.user
        instance.save()
        return instance
    

def mostrar_imagen(obj):
    if obj.imagen:
        return "<img src='%s' alt='img'></a>" % obj.get_image_url()
    return "<span>Sin imagen</sapan>"
        

mostrar_imagen.short_description = 'Imagen'
mostrar_imagen.allow_tags = True

admin.site.register(Post, PostAdmin)


#---------------------------------------------------------------
class CategoryAdmin(admin.ModelAdmin):
    list_display    = (mostrar_imagen,'nombre')
    search_fields   = ('nombre',)
    prepopulated_fields = {'slug': ('nombre',)}

admin.site.register(Category, CategoryAdmin)