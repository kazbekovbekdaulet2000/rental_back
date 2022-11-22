from django.contrib import admin
from article.models.article import Article
from article.models.grants import GrantForm


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title_ru", "title_kk", "active", "order")
    prepopulated_fields = {"slug": ("title_ru",)}
    search_fields = ('title_ru', 'title_kk', 'body_ru', 'body_kk', 'tags')


class GrantFormAdmin(admin.ModelAdmin):
    readonly_fields = ('full_name', 'phone', 'instagram_url', 'portfolio_url',
                       'description', 'file', 'date', 'comment', 'approved')
    list_display = ('full_name', 'phone', 'instagram_url', 'date', 'approved')

admin.site.register(Article, ArticleAdmin)
admin.site.register(GrantForm, GrantFormAdmin)