from django.contrib import admin
from main.models import Category, Article
from main.forms import CategoryForm, ArticleForm
from froala_editor.widgets import FroalaEditor


class CategoryAdmin(admin.ModelAdmin):
	form = CategoryForm
	fields = ['name', 'active', 'order', 'color']


class ArticleAdmin(admin.ModelAdmin):
	form = ArticleForm
	fields = ['name', 'content', 'category', 'is_top', 'is_main', 'img']
	

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
