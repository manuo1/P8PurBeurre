from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from app_products.models import FoodCategory, FoodProduct
from django.contrib.auth import get_user_model, login

class TestAppProductsViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.User = get_user_model()
        self.test_category_1 = FoodCategory.objects.create(
                category_name = 'test_category'
        )
        self.test_product_1 = FoodProduct.objects.create(
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
        self.test_product_1.categories.add(self.test_category_1)
        self.test_factory = RequestFactory()
        self.test_user_1 = self.User.objects.create_user(
                                    username = 'test_name',
                                    email = 'test_mail@mail.com',
                                    password = 'test_password')
        self.test_user_1.favorites.add(self.test_product_1)

    def test_if_index_view_return_index_template(self):
        response = self.client.get(reverse('indexPage'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_if_search_view_return_search_template(self):
        response = self.client.get(reverse('search'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')

    def test_if_search_view_POST_return_search_template(self):
        response = self.client.post(reverse('search'), args = 'example')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')

    def test_if_product_details_view_return_product_details_template(self):
        id = self.test_product_1.id
        response = self.client.get(reverse('productDetailsPage', args = [id]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_details.html')

    def test_if_product_details_view_return_404(self):
        response = self.client.get(reverse('productDetailsPage', args = [0]))
        self.assertEquals(response.status_code, 404)

    def test_if_substitutes_view_return_substitutes_template(self):
        id = self.test_product_1.id
        response = self.client.get(reverse('substitutesPage', args = [id]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'substitutes.html')

    def test_if_substitutes_view_return_404_if_no_product_to_display(self):
        response = self.client.get(reverse('substitutesPage', args = [0]))
        self.assertEquals(response.status_code, 404)

    def test_if_favorites_view_unlogged_return_302(self):
        request = self.test_factory.get(reverse('FavoritesPage'))
        request.user = self.test_user_1
        response = self.client.get(reverse('FavoritesPage'))
        self.assertEquals(response.status_code, 302)

    def test_if_favorites_view_without_args_return_favorites_template(self):
        request = self.test_factory.get(reverse('FavoritesPage'))
        request.user = self.test_user_1
        self.client.login(username = 'test_name',password = 'test_password')
        response = self.client.get(reverse('FavoritesPage'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'favorites.html')

    def test_if_favorites_view_with_args_return_favorites_template(self):
        id = self.test_product_1.id
        request = self.test_factory.get(reverse('AddFavorites', args = [id]))
        request.user = self.test_user_1
        self.client.login(username = 'test_name',password = 'test_password')
        response = self.client.get(reverse('AddFavorites', args = [id]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'favorites.html')

    def test_if_favorites_view_with_args_return_404(self):
        request = self.test_factory.get(reverse('AddFavorites', args = [0]))
        request.user = self.test_user_1
        self.client.login(username = 'test_name',password = 'test_password')
        response = self.client.get(reverse('AddFavorites', args = [0]))
        self.assertEquals(response.status_code, 404)

    def test_if_legal_disclaimers_view_return_legal_disclaimers_template(self):
        response = self.client.get(reverse('LegalDisclaimersPages'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'legal_disclaimers.html')

    def test_if_contact_view_return_index_template(self):
        response = self.client.get(reverse('contact'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
