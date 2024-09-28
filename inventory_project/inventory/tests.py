from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Item

class ItemTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item_data = {'name': 'Item1', 'description': 'Description1'}
        self.item = Item.objects.create(**self.item_data)

    def test_create_item(self):
        response = self.client.post(reverse('create_item'), self.item_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_item(self):
        response = self.client.get(reverse('item_detail', kwargs={'pk': self.item.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
