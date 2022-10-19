from rest_framework import generics
from rest_framework import permissions
from product.models.category import Category
from product.serializers.category import CategorySerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all().order_by('created_at')
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny, ]
    pagination_class = None