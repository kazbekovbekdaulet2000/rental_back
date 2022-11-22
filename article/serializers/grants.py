
from rest_framework import serializers
from article.models.grants import GrantForm


class GrantFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrantForm
        fields = "__all__"
