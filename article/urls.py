from django.urls import path
from article.views.articles import ArticlesList, ArticleDetail
from article.views.grants import GrantFormCreate


urlpatterns = [
    path('articles/', ArticlesList.as_view()),
    path('articles/<slug:slug>/', ArticleDetail.as_view()),
    path('grants/', GrantFormCreate.as_view())
]
