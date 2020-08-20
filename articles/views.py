from django.shortcuts import render

from articles.models import Article, Author, Category


def hello_world(request):
    articles = Article.objects.all().order_by("-published_at")
    return render(request, template_name="index.html", context={"articles":articles})

def list_articles(request):
    articles = Article.objects.all().order_by("-published_at")
    return render(request, template_name="articles/article-list.html", context={"articles":articles})

def display_article(request, article_id):
    article = Article.objects.get(id=article_id)
    author = article.AuthorID
    return render(request, template_name="articles/article_display.html",
                  context={"article": article, "author": author})

def list_categories(request):
    categories = Category.objects.all()
    return render(request, template_name="articles/category-list.html", context={"categories": categories})

def list_single_category(request, category_id):
    articles = Article.objects.filter(categoryID=category_id)
    return render(request, template_name="articles/article-list.html", context={"articles":articles})

def author_display(request, author_id):
    author= Author.objects.get(id = author_id)
    articles = Article.objects.filter(AuthorID=author_id)
    return render(request, template_name="articles/author-display.html",
                  context={"author": author, "articles": articles})

