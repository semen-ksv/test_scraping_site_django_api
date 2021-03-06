from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .tasks import scrape_cur
from .models import ProductItem
from .serializers import ProductItemSerializer



def main_index(request):
    """Create main index page url('/')"""

    if request.method == 'GET':
        scrape_cur.delay()

        return render(request, 'citrys_scraping/index.html')


class ItemsListView(ListAPIView):
    """Output list of all items"""

    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type', 'price', 'cashback']


class FilterPhoneItemView(ListAPIView):
    """Output list of all items"""

    queryset = ProductItem.objects.filter(type='iPhone')
    serializer_class = ProductItemSerializer


class FilterNotebookItemView(ListAPIView):
    """Output list of all items"""

    queryset = ProductItem.objects.filter(type='Notebook')
    serializer_class = ProductItemSerializer
