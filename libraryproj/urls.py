"""libraryproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from articles import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile_view, name='user_profile'),
    path('accounts/signup/', views.user_signup, name="user_signup"),


    path('', views.hello_world, name="index"),
    path('articles', views.list_articles, name="articles list"),
    path('articles/<int:article_id>',views.display_article, name="article display"),

    path('categories', views.list_categories, name='categories'),
    path('categories/<int:category_id>', views.list_single_category, name='category display'),

    path('author/<int:author_id>', views.author_display, name='author display'),

    path("search", views.search, name="search"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
