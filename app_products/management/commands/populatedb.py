from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from app_products.models import FoodProduct, FoodCategory
from .offdata.download import Download
from .offdata.cleaner import Cleaner
from app_products.models import FoodCategory, FoodProduct


class Command(BaseCommand):
    help = """Populate database with food products from the Open Food Fact API,
            Requires a quantity of food products to be added,
            Example to add 10 products: \"python manage.py populatedb 10\" """

    def add_arguments(self, parser):
        parser.add_argument('quantity', type=int)

    def handle(self, *args, **options):
        food_data = self.get_food_products_data(options['quantity'])
        self.add_food_products_in_database(food_data)


    def get_food_products_data(self, quantity):
        download = Download()
        cleaner = Cleaner()
        data_to_add = []
        page_number = 1
        self.stdout.write('Téléchargement des aliments...')
        while len(data_to_add) < quantity:
            qty=len(data_to_add)
            raw_products_list = download.raw_data(page_number)
            cleaned_products_list = cleaner.clean(raw_products_list)
            data_to_add.extend(cleaned_products_list)
            if len(data_to_add) >= quantity:
                data_to_add = (data_to_add[:quantity])
                break
            page_number+=1
        self.stdout.write('{} aliments téléchargés'.format(len(data_to_add)))
        return data_to_add


    def add_food_products_in_database(self,data_to_add):
        for product in data_to_add:
            """add product to the FoodProduct table"""
            product_to_add = FoodProduct(**product['data'])
            try:
                product_to_add.save()
            except IntegrityError:
                pass
            """adds the product categories in the FoodCategory table"""
            for category in product['categories']:
                category_to_add = FoodCategory(category_name = category)
                try:
                    category_to_add.save()
                except IntegrityError:
                    pass
                """ associates the product to its categories """
                """ first gets objects in the tables to get ids """
                category_to_associate = FoodCategory.objects.get(
                    category_name=category)
                product_to_associate = FoodProduct.objects.get(
                    barcode=product['data']['barcode'])
                """ then builds the association"""
                product_to_associate.categories.add(category_to_associate)

        self.stdout.write('{} aliments présents dans la base'.format(
                                    FoodProduct.objects.all().count()))
        self.stdout.write('{} categories présentes dans la base'.format(
                                    FoodCategory.objects.all().count()))
