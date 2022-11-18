
from article.models.article import Article
from rest_framework import serializers
from product.models.product import Product
from product.serializers.product import BaseProductSerializer


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title_ru', 'title_kk', 'body_ru', 'body_kk', 'tags', 'slug', 'image_ru', 'image_kk', 'outer_url')


class ArticleDetailSerializer(serializers.ModelSerializer):
    products = BaseProductSerializer(many=True)
    
    def to_representation(self, instance):
        instance.products = Product.objects.filter(id__in=instance.products, active=True)
        self.fields['products'] = BaseProductSerializer(many=True, read_only=True, context={"request": self.context['request']})
        return super(ArticleDetailSerializer, self).to_representation(instance)

    class Meta:
        model = Article
        exclude = ('active', 'updated_at', 'created_at')