from datetime import datetime, timedelta
from main.models import Article


def get_popular():
	return Article.objects.filter(created_at__gte=datetime.now() - timedelta(days=4)).order_by('-reading_count')[:4]


def get_last_articles():
	return Article.objects.order_by("-created_at")[:20]
