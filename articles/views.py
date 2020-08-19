from datetime import datetime
from django.shortcuts import render

from articles.models import Article


def hello_world(request):
    our_context = {"time": datetime.now()}
    return render(request, template_name="index.html", context=our_context)

def list_articles(request):
    articles = Article.objects.all()
    return render(request, template_name="articles/article-list.html", context={"articles":articles})

def display_article(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, template_name="articles/article_display.html", context={"article": article})

