from django.urls import path
from article.views.articles import ArticlesList, ArticleDetail


urlpatterns = [
  path('articles/', ArticlesList.as_view()),
  path('articles/<slug:slug>/', ArticleDetail.as_view())
]
