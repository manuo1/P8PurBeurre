from django.test import RequestFactory, TestCase
from app_products.models import FoodProductsManager,FoodProduct
from app_users.models import UsersManager
from app_products.forms import ProductSearchFormManager
from app_products.views import index, search
from _pytest.monkeypatch import MonkeyPatch

class UnitTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.monkeypatch = MonkeyPatch()

        self.test_product = FoodProduct.objects.create(
                id = 123,
                product_name = 'test_product_name',
                nutriscore = 'z',
                barcode = '123',
                image_url = 'https://static.openfoodfacts.org/test_image.jpg',
                energy_kj = '123',
                energy_kcal = '123',
                protein = '123',
                glucid = '123',
                lipid = '123',
                fiber = '123',
                salt = '123'
        )


    def mock_get_search_in(self, ProductSearchFormManager):
        return 'test product name'

    def mock_find_matching_food_products(self, FoodProductsManager):
        class MockProduct:
            def __init__(self):
                self.id = 123,
                self.product_name = 'test product name',
                self.nutriscore = 'z',
                self.barcode = '123',
                self.image_url = 'https://static.openfoodfacts.org/test_image.jpg',
                self.energy_kj = '123',
                self.energy_kcal = '123',
                self.protein = '123',
                self.glucid = '123',
                self.lipid = '123',
                self.fiber = '123',
                self.salt = '123'

        product = MockProduct()
        matching_list=[product]
        return matching_list

    def test_index(self):
        request = self.factory.get('/')
        response = index(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Du gras, oui, mais de' in str(response.content))

    def test_search(self):
        request = self.factory.get('/search')
        request.method = 'POST'
        #request.POST = request.POST.copy()

        self.monkeypatch.setattr(
            'app_products.forms.ProductSearchFormManager.get_search_in',
            self.mock_get_search_in
        )
        self.monkeypatch.setattr(
            ('app_products.models.FoodProductsManager.'
            'find_matching_food_products'),
            self.mock_find_matching_food_products
        )
        response = search(request)
