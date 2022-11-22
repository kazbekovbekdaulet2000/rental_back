from rest_framework import generics
from rest_framework import permissions
from article.serializers.grants import GrantFormSerializer
from rest_framework.parsers import MultiPartParser


class GrantFormCreate(generics.CreateAPIView):
    parser_classes = [MultiPartParser, ]
    serializer_class = GrantFormSerializer
    permission_classes = [permissions.AllowAny, ]