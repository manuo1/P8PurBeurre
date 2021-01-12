import unittest
from unittest import mock
from unittest.mock import Mock, patch
from django.test import RequestFactory, TestCase
from app_products.models import FoodProductsManager,FoodProduct
from app_products.forms import ProductSearchFormManager
from app_products.views import index, search

class ViewsUnitTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index(self):
        request = self.factory.get('/')
        response = index(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Du gras, oui, mais de', str(response.content))

    @mock.patch(
        'app_products.views.ProductSearchFormManager.get_search_in',
        return_value='test product name')
    @mock.patch(
        'app_products.views.FoodProductsManager.find_matching_food_products_to',
        return_value=[Mock()], autospec=True)
    def test_search(self,mock_f_manager_get,mock_fp_manager_find):
        request = self.factory.get('/search')
        request.method = 'POST'
        response = search(request)
