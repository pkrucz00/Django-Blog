from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

from articles.models import Article, Author, Category


def hello_world(request):
    articles = Article.objects.all().order_by("-published_at")
    return render(request, template_name="index.html", context={"articles":articles})

def list_articles(request):
    articles = Article.objects.all().order_by("-published_at")
    return render(request, template_name="articles/article_list.html", context={"articles":articles})

def display_article(request, article_id):
    article = Article.objects.get(id=article_id)
    author = article.AuthorID
    return render(request, template_name="articles/article_display.html",
                  context={"article": article, "author": author})

def list_categories(request):
    categories = Category.objects.all()
    return render(request, template_name="articles/category_list.html", context={"categories": categories})

def list_single_category(request, category_id):
    articles = Article.objects.filter(categoryID=category_id)
    return render(request, template_name="articles/article_list.html", context={"articles":articles})

def author_display(request, author_id):
    author= Author.objects.get(id = author_id)
    articles = Article.objects.filter(AuthorID=author_id)
    return render(request, template_name="articles/author_display.html",
                  context={"author": author, "articles": articles})

def profile_view(request):
    return render(request, template_name="registration/log_in_greeting.html")


def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, template_name="registration/signup_complete.html")
    else:
        # tutaj obsługujemy przypadek kiedy użytkownik pierwszy raz wyświetlił stronę
        form = UserCreationForm()

    # na końcu zwracamy wyrenderowanego HTMLa
    return render(request, template_name="registration/signup_form.html", context={'form': form})

def logout(request):
    logout(request)
    return render(request, template_name="registration/logged_out.html")

def search(request):
    query = request.GET.get("q")
    if query:
        article_results = Article.objects.filter(title__icontains=query)
    else:
        article_results = []
    return render(request, template_name="articles/search_results.html",
                  context={"articles": article_results})