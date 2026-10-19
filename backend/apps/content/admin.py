from django.contrib import admin
from .models import Article, ArticleCategory, ArticleTag

admin.site.register((Article, ArticleCategory, ArticleTag))
