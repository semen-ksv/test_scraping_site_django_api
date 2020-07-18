from rest_framework import serializers
from .models import ProductItem

class ProductItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductItem
        fields = ('slug', 'title', 'date_posted', 'total_likes')
        read_only_fields = fields