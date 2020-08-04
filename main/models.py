from django.db import models
from pytils.translit import slugify
from django.contrib.auth import get_user_model
from froala_editor.fields import FroalaField


class Category(models.Model):
	name = models.CharField(max_length=511)
	slug = models.CharField(max_length=63, blank=True)
	active = models.BooleanField(default=True)
	color = models.CharField(max_length=8, null=True)
	order = models.PositiveIntegerField(default=1)
	
	def __str__(self):
		return self.name
	
	def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
		
		self.slug = slugify(self.name)[:63]
		
		initial_slug = self.slug
		i = 1
		while Category.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
			self.slug = initial_slug + "-" + str(i)
			i += 1
			
		return super(Category, self).save(force_insert=force_insert, force_update=force_update,
		                                  using=using, update_fields=update_fields)

	
class Article(models.Model):
	name = models.TextField()
	slug = models.SlugField(max_length=255, blank=True)
	content = models.TextField()
	category = models.ForeignKey(Category, related_name="articles", on_delete=models.SET_NULL, null=True)
	subcategories = models.ManyToManyField(Category, related_name="subcategories", blank=True)
	is_main = models.BooleanField(default=False)
	is_top = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.SET_NULL)
	img = models.ImageField(upload_to='images/', verbose_name=u"Головне зображення", null=True, blank=True)
	reading_count = models.PositiveIntegerField(default=0)
	
	def __str__(self):
		return self.name
	
	def save(self, force_insert=False, force_update=False, using=None,
	         update_fields=None):
		self.slug = slugify(self.name)[:63]
		
		initial_slug = self.slug
		i = 1
		while Article.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
			self.slug = initial_slug + "-" + str(i)
			i += 1
		
		return super(Article, self).save(force_insert=force_insert, force_update=force_update,
		                                 using=using, update_fields=update_fields)
