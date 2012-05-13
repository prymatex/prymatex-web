# -*- coding: utf-8 -*-


from datetime import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from apps.accounts.models import UserProfile

from utiles.utiles import slugify


class EntryTag(models.Model):
	nombre = models.CharField(max_length=80)
	slug = models.SlugField(unique=True)
	
	def save(self, force_insert=False, force_update=False):
		self.nombre = self.nombre.lower()
		super(EntryTag,self).save()
		
	def __unicode__(self):
		return self.nombre

		
		
	class Meta:
		verbose_name_plural = 'Tags'
		ordering = ('nombre',)
		get_latest_by = 'id'
	

class Category(models.Model):
	nombre = models.CharField(max_length=200)
	padre = models.ForeignKey('self', null=True, blank=True)
	slug = models.SlugField(unique=True)
	imagen = models.ImageField(upload_to="images/category/", null=True, blank=True)
	
	def get_image_url(self):
		if self.image:
			return "%s%s" % (settings.MEDIA_URL, self.imagen)
         
	class Meta:
		verbose_name_plural = 'Categorias'
		ordering = ('nombre',)
		get_latest_by = 'id'
	
	def get_absolute_url(self):
		return "/blog/category/%s/" % self.slug 
	
	def __unicode__(self):
		return self.nombre
	
	

class Post(models.Model):
	
	STATUS_CHOICES = (
        (1, _('Draft')),
        (2, _('Public')),
    )
	
	#cache del src del avatar
	avatar = None
	
	titulo 			= models.CharField(max_length=200)
	pub_date 		= models.DateTimeField(_('Fecha de creacion'), default=datetime.now, editable=False)
	updated_at      = models.DateTimeField(_('updated at'), editable=False)
	  
	slug 			= models.SlugField(unique_for_date='pub_date')
	status          = models.IntegerField(_('Estado'), choices=STATUS_CHOICES, default=2)
	allow_comments  = models.BooleanField(_('Acepta comentarios'), default=False)
	
	texto 	= models.TextField(help_text="Usar HTML crudo")
	

	autor 			= models.ForeignKey(User, editable=False, related_name="added_post")

	lecturas 		= models.IntegerField(default=0, editable=False)
	votos_positivos = models.IntegerField(default=0, editable=False)
	votos_negativos = models.IntegerField(default=0, editable=False)
	
	category       = models.ForeignKey(Category,related_name="from_category", blank=True, null=True)
	
	tags            = models.ManyToManyField(EntryTag, null=True, blank=True)
	
	
	class Meta:
		verbose_name_plural = 'posts'
		ordering = ('-pub_date',)
		get_latest_by = 'pub_date'

		
	def get_absolute_url(self):
		return "/blog/%s/%s/" % (self.pub_date.strftime("%d/%m/%Y"), self.slug)
	
	
	def save(self, force_insert=False, force_update=False):
		if getattr(self, 'autor_id', None) is None:
			self.autor_id = threadlocals.get_current_user().id
		self.updated_at = datetime.now()
		super(Post, self).save(force_insert, force_update)

		
	
	def delete(self):
		#decremento las lecturas de los tags que tiene este post
		super(Post, self).delete()
	
	
	def post_leido(self):
		"""
		Este metodo es llamado cuando el Post es leido entonces
		incrementamos el contador de lecutras en 1
		Y le decimos al los tags que tiene el post que se incremente
		tambien su lectura
		"""
		self.lecturas+=1
		self.save()
	
	def __unicode__(self):
		return self.titulo
	
	def get_category_url(self):
		return "/blog/category/%s/" % self.category.slug
	
	def get_autor_avatar(self):
		if self.avatar:
			return self.avatar
		profile = UserProfile.getUserProfile(self.autor)
		gravatar_url =  profile.get_grevatar_src()
		self.avatar = gravatar_url
		return self.avatar
	
	
		
		
	def texto_corto(self):
		"""
		<!-- pagebreak -->
		"""
		import re
		#resp = re.search('^(.+)<!-- pagebreak -->' ,self.texto)
		#resp = re.search('^(?P<short_text>[\s\S]+)(\<\!-- \s?pagebreak\s? --\>)(?P<body>[\s\S]*)$' ,self.texto)
		#print re
		compile_obj = re.compile('^(?P<short_text>[\s\S]+)(\<\!-- \s?pagebreak\s? --\>)(?P<body>[\s\S]*)$',  re.IGNORECASE| re.MULTILINE| re.VERBOSE)
		resp = compile_obj.search(self.texto)
		"""
		if hasattr(resp, 'group'):
			return resp.group(0)
		"""
		try:
			return resp.group('short_text')
		except:
			pass
			

		
	  