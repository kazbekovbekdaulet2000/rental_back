from django.contrib import admin
from article.models.article import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title_ru", "title_kk", "active", "order")
    prepopulated_fields = {"slug": ("title_ru",)}
    search_fields = ('title_ru', 'title_kk', 'body_ru', 'body_kk', 'tags')


admin.site.register(Article, ArticleAdmin)