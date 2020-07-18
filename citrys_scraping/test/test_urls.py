from rest_framework.test import APISimpleTestCase
from django.urls import reverse, resolve
from citrys_scraping.views import main_index, ItemsListView, FilterNotebookItemView, FilterPhoneItemView


class TestUrls(APISimpleTestCase):
    """test all urls from citrys_scraping"""

    def test_index_page_url(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, main_index)

    def test_list_items_url(self):
        url = reverse('items-list')
        self.assertEqual(resolve(url).func.view_class, ItemsListView)

    def test_phone_list_url(self):
        url = reverse('phone-list')
        self.assertEqual(resolve(url).func.view_class, FilterPhoneItemView)

    def test_notebook_list_url(self):
        url = reverse('notebook-list')
        self.assertEqual(resolve(url).func.view_class, FilterNotebookItemView)
