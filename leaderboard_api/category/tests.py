from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from category.models import Category

User = get_user_model()

class CategoryAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='tuser', password='pass123')
        self.client.force_authenticate(user=self.user)   # makes requests authenticated

    def test_create_and_list_category(self):
        url = '/api/categories/'
        data = {'name': 'Puzzle'}
        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)

        # now list
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        # DRF may return a paginated response (dict with 'results') or a plain list.
        data = res.data
        if isinstance(data, dict) and 'results' in data:
            results = data['results']
        else:
            results = data

        # ensure we have at least one returned object and it matches
        self.assertTrue(len(results) >= 1)
        self.assertEqual(results[0]['name'], 'Puzzle')