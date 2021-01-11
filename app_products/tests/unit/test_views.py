from django.test import RequestFactory, TestCase
from app_products.models import FoodProductsManager, FoodProduct
from app_products.views import index, search
from unittest.mock import patch

class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index(self):
        request = self.factory.get('/')
        response = index(request)
        self.assertEqual(response.status_code, 200)
    """
    def test_search(self):
        request = self.factory.get('/search')
        request.method = 'POST'
        request.POST = request.POST.copy()
        request.POST['search'] = 'test'
        response = search(request)
        print(response.content)
    """
