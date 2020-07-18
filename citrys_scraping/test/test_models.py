from django.contrib.contenttypes.models import ContentType
from rest_framework.test import APITestCase
from time import time
from citrys_scraping.models import ProductItem


class TestProductItemtModel(APITestCase):
    """ProductItem model testing fields, slug generations"""

    def setUp(self) -> None:

        self.products = ProductItem.objects.create(
            name="phone",
            link='link/to/phone',
            image_link='link/to/phone/image',
            price=100,
            cashback=10,
            product_html='<html><html/>'
        )

    def test_post_fields(self):
        record_product = ProductItem.objects.get(id=self.products.id)
        self.assertEqual(record_product, self.products)

        record2_product = ProductItem.objects.get(name=self.products.name)
        self.assertEqual(record2_product, self.products)

        record3_product = ProductItem.objects.get(link=self.products.link)
        self.assertEqual(record3_product, self.products)


