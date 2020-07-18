from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.utils import json
from ..models import ProductItem
from ..serializers import ProductItemSerializer

client = APIClient()

class GetAllItemsTest(APITestCase):
    """Test module for GET all posts API"""

    def setUp(self):
        self.item = ProductItem()
        self.item.name = 'New iphone'
        self.item.link = 'link/to/phone'
        self.item.image_link = 'link/to/phone/image'
        self.item.price = 100
        self.item.cashback = 10
        self.item.specifications = '<html><html/>'
        self.item.save()

    def test_get_all_item(self):
        # get API response
        response = client.get(reverse('items-list'))
        # get data from db
        post = ProductItem.objects.all()
        serializer = ProductItemSerializer(post, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class FilterItemsTest(APITestCase):
    """Test module for GET all posts API"""

    def setUp(self):
        self.item_phone = ProductItem()
        self.item_phone.name = 'New iphone'
        self.item_phone.type = 'iPhone'
        self.item_phone.link = 'link/to/phone'
        self.item_phone.image_link = 'link/to/phone/image'
        self.item_phone.price = 100
        self.item_phone.cashback = 10
        self.item_phone.specifications = '<html><html/>'
        self.item_phone.save()

        self.item_notebook = ProductItem()
        self.item_notebook.name = 'New notebook'
        self.item_notebook.type = 'Notebook'
        self.item_notebook.link = 'link/to/notebook'
        self.item_notebook.image_link = 'link/to/notebook/image'
        self.item_notebook.price = 120
        self.item_notebook.cashback = 15
        self.item_notebook.specifications = '<html>notebook<html/>'
        self.item_notebook.save()

    def test_get_all_phones(self):
        # get API response
        response = client.get(reverse('phone-list'))
        # get data from db
        post = ProductItem.objects.filter(type='iPhone')
        serializer = ProductItemSerializer(post, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_notebook(self):
        # get API response
        response = client.get(reverse('notebook-list'))
        # get data from db
        post = ProductItem.objects.filter(type='Notebook')
        serializer = ProductItemSerializer(post, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
