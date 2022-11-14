from rest_framework import generics
from rest_framework import permissions
from article.models.article import Article
from article.serializers.articles import ArticleSerializer, ArticleDetailSerializer


class ArticlesList(generics.ListAPIView):
    queryset = Article.objects.filter(active=True)
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny, ]
    pagination_class = None


class ArticleDetail(generics.RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Article.objects.filter(active=True)
    serializer_class = ArticleDetailSerializer
    permission_classes = [permissions.AllowAny, ]