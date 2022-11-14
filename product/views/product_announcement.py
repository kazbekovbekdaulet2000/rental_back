from rest_framework import generics
from rest_framework import permissions
from product.models.product_announcement import ProductAnnouncement
from product.serializers.product import BaseProductSerializer


class NewProductsList(generics.ListAPIView):
    queryset = ProductAnnouncement.objects.all()
    serializer_class = BaseProductSerializer
    permission_classes = [permissions.AllowAny, ]
    pagination_class = None

    def get_queryset(self):
        products = []
        for announce in super().get_queryset():
            products.append(announce.product)
        return products