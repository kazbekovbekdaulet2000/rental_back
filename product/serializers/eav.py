from rest_framework import serializers

from product.models.eav import Attribute, Value


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('id', 'attribute_ru', 'attribute_kk')


class ValueSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer(read_only=True)

    class Meta:
        model = Value
        fields = ('id', 'attribute', 'value_ru', 'value_kk')
