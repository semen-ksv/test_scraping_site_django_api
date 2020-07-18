from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import ProductItem



class ItemsListView(ListAPIView):
    """Output list of all items"""

    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer