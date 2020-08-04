from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from main.models import Category, Article
from main.utils import get_popular, get_last_articles


def index(request):
	top_posts = Article.objects.filter(is_top=True).order_by("-created_at")[:2]
	last_main_posts = Article.objects.exclude(pk__in=top_posts).filter(is_main=True).order_by("-created_at")[:13]
	return render(request, "index.html", {
		"top_posts": top_posts,
		"last_main_posts": last_main_posts,
	})


def category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	first_post = Article.objects.filter(category=category, img__isnull=False).order_by("-created_at").first()
	
	return render(request, "category.html", {
		"category": category,
		"first_post": first_post,
	})


def post(request, slug):
	post = get_object_or_404(Article, slug=slug)
	post.reading_count += 1
	post.save()
	
	return render(request, "blog-post.html", {
		"post": post,
	})


def privacy(request):
	return render(request, "privacy.html")


def about(request):
	return render(request, "about.html")


def contacts(request):
	return render(request, "contact.html")


def search(request):
	term = request.GET.get("search")
	search_posts = Article.objects.filter(Q(name__search=term) | Q(content__search=term))
	return render(request, "search.html", {
		"search_posts": search_posts,
		"term": term,
	})
