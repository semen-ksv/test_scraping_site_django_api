from rest_framework import serializers
from .models import ProductItem

class ProductItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductItem
        fields = ('name', 'link', 'image_link', 'price', 'cashback', )
        read_only_fields = fields
