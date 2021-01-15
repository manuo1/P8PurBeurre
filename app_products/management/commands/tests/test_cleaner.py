from unittest import mock
from django.test import TestCase
from ..offdata.cleaner import Cleaner
from ..offdata.constants import (
    ESSENTIAL_PRODUCT_DATA as product_fields_list,
    USEFUL_NUTRIENTS_DATA as nutrient_fields_list,
    MAXIMUM_QUANTITY_OF_CATEGORIES_TO_KEEP_PER_PRODUCT as max_of_categories,
    PRODUCT_TO_ADD_MODEL as product_model,
    TEST_PRODUCT
)


class CleanerUnitTest(TestCase):
    def setUp(self):
        self.categories_expected_list = [
            'Categories-01',
            'Categories âé 02',
            'Cat03',
            'i\'m a category 04',
            'tested-cat_05',
            'Testing a good category name 06'
        ]

    def test_clean(self):
        """ create a testing raw_products_list """
        raw_products_list = []
        """adding 20 products products in raw_products_list"""
        """ only 10 are valid """
        while (len(raw_products_list)) < 20:
            temp_product = TEST_PRODUCT.copy()
            temp_product['product_name_fr'] =(
                'test name ' + str(len(raw_products_list)+1))
            if len(raw_products_list)>=10:
                temp_product['product_name_fr'] = (
                    temp_product['product_name_fr'] + ' bad')
            if len(raw_products_list)>=10:
                del temp_product['code']
            elif len(raw_products_list)>=15:
                temp_product['code'] = ''
            raw_products_list.append(temp_product)
        """
        with mock.patch(
            'app_products.management.commands.offdata.cleaner.Cleaner'
            '.all_data_is_in',
                return_value=True,
            ):
        """
            #Cleaner.clean(Cleaner,raw_products_list)



    def test_change_field_names(self):
        """ test if new product fields match with model_product """
        tested_product = Cleaner.change_field_names(Cleaner,product_model)
        for key, value in tested_product.items():
            self.assertEqual(key, value)

    def test_nutrients(self):
        """Verify that all nutrients cleaned are equivalent """
        """to the nutrient data required."""
        cleaned_nutrients = Cleaner.nutrients(Cleaner,TEST_PRODUCT)
        cleaned_nutrients_list = list(cleaned_nutrients.keys())
        cleaned_nutrients_list.sort()
        nutrient_fields_list.sort()
        self.assertEqual(cleaned_nutrients_list, nutrient_fields_list)

    def test_categories(self):
        """check that the created category list """
        """corresponds to the expected one"""
        returned_list = Cleaner.categories(Cleaner,TEST_PRODUCT)
        self.assertEqual(returned_list, self.categories_expected_list)

    def test_all_data_is_in_return_true(self):
        """ check if it return true when all are present """
        self.assertTrue(Cleaner.all_data_is_in(Cleaner,TEST_PRODUCT))

    def test_all_data_is_in_return_false_when_1_field_missing(self):
        """ check if it return false when a field is missing """
        bad_product = TEST_PRODUCT.copy()
        del bad_product["categories"]
        self.assertFalse(Cleaner.all_data_is_in(Cleaner,bad_product))

    def test_all_data_is_in_return_false_when_1_field_is_empty(self):
        """ check if it return true when a value is empty """
        bad_product = TEST_PRODUCT.copy()
        bad_product["product_name_fr"] = ''
        self.assertFalse(Cleaner.all_data_is_in(Cleaner,bad_product))
