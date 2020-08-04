from django.urls import path
from main.views import index, category, post, privacy, about, contacts, search


urlpatterns = [
	path('', index, name="index"),
	path('category/<slug>', category, name="category"),
	path('article/<slug>', post, name="article"),
	path('privacy', privacy, name="privacy"),
	path('about', about, name="about"),
	path('contacts', contacts, name="contacts"),
	path('search', search, name="search"),
]
