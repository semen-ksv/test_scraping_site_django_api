from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView
from rest_framework.generics import ListAPIView
from .tasks import scrape_async, scrape_cur, some
from .models import ProductItem
from .serializers import ProductItemSerializer
from .scraper import find_iphone, find_notebook
from .forms import ScrapForm


def main_index(request):
    """Create main index page url('/')"""

    if request.method == 'GET':
        print('start')
        # scrape_cur.delay()
        print('finihs')
        return render(request, 'citrys_scraping/index.html')



# class StartPageView(FormView):
#     template_name = 'citrys_scraping/index.html'
#     form_class = ScrapForm
#
#     def get_success_url(self):
#         return reverse("index")
#
#     def form_valid(self, form):
#         scrape_async.delay()
#         return super(StartPageView, self).form_valid(form)
#

class ItemsListView(ListAPIView):
    """Output list of all items"""

    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer


class FilterPhoneItemView(ListAPIView):
    """Output list of all items"""

    queryset = ProductItem.objects.filter(type='iPhone')
    serializer_class = ProductItemSerializer


class FilterNotebookItemView(ListAPIView):
    """Output list of all items"""

    queryset = ProductItem.objects.filter(type='Notebook')
    serializer_class = ProductItemSerializer
