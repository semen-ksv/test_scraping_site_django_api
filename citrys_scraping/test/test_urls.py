from rest_framework.test import APISimpleTestCase
from django.urls import reverse, resolve
from citrys_scraping.views import *


class TestUrls(APISimpleTestCase):
    """test all urls from post_api"""

    def test_index_page_url(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, main_index)
#
    def test_post_create_url(self):
        url = reverse('items-list')
        self.assertEqual(resolve(url).func.view_class, ItemsListView)
#
#     def test_post_update_url(self):
#         url = reverse('post-update', args=['post_slug', ])
#         self.assertEqual(resolve(url).func.view_class, PostUpdateView)
#

