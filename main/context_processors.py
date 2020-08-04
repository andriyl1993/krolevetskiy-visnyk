from main.models import Category
from main.utils import get_popular, get_last_articles


def header_values(_):
	cats = Category.objects.filter(active=True).order_by("order")
	return {
		"categories": cats,
	}


def most_popular(_):
	return {
		"most_popular": get_popular(),
	}


def last_posts(_):
	return {
		"last_posts": get_last_articles(),
	}
