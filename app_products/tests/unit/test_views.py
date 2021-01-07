from django.test import RequestFactory, TestCase
from app_products.views import index

class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_index(self):
        request = self.factory.get('/')
        response = index(request)
        self.assertEqual(response.status_code, 200)
"""
    def test_search(self):
        print('starting unit test search')
        request = self.factory.get('/search')
        request.method = 'POST'

        class MockProductSearchForm:
            def __init__(self):
                pass
"""
