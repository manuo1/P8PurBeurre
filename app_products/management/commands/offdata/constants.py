API_OFF_URL = "https://fr.openfoodfacts.org/cgi/search.pl?"

API_OFF_PARAMS = {
    'action': 'process',
    'sort_by': 'unique_scans_n',
    'json': 'true',
    'page': 1,
    'page_size': 1000,
}
MAXIMUM_QUANTITY_OF_CATEGORIES_TO_KEEP_PER_PRODUCT = 6
ESSENTIAL_PRODUCT_DATA = [
    'product_name_fr',
    'nutrition_grade_fr',
    'code',
    'image_url',
    'categories',
    'nutriments',
]
USEFUL_NUTRIENTS_DATA = [
    'energy-kj_100g',
    'energy-kcal_100g',
    'proteins_100g',
    'carbohydrates_100g',
    'fat_100g',
    'fiber_100g',
    'salt_100g',
]
PRODUCT_TO_ADD_MODEL = {
    'product_name_fr': 'product_name',
    'nutrition_grade_fr': 'nutriscore',
    'code': 'barcode',
    'image_url': 'image_url',
    'energy-kj_100g': 'energy_kj',
    'energy-kcal_100g': 'energy_kcal',
    'proteins_100g': 'protein',
    'carbohydrates_100g': 'glucid',
    'fat_100g': 'lipid',
    'fiber_100g': 'fiber',
    'salt_100g': 'salt',
}

TEST_PRODUCT = {
    "useless_1": "nothing",
    "useless_2": 123,
    "useless_3": "nothing",
    "useless_4": ["nothing1","nothing2"],
    "useless_5": {"nothing": "nothing1"},
    "product_name_fr": "my name",
    "nutrition_grade_fr": "e",
    "code": "1234567891234",
    "image_url": "https://static.openfoodfacts.org/images/test.jpg",
    "categories":
        "Categories-01, Categories âé 02, Cat03, i'm a category 04,"
        " tested-cat_05, Testing a good category name 06",

    "nutriments": {
            "energy-kj_100g": 123,
            "energy-kcal_100g": 1.23456,
            "proteins_100g": 123,
            "carbohydrates_100g": 1.23,
            "fat_100g": 123,
            "fiber_100g": 1.23456,
            "salt_100g": 123,
            "nutr-useless_1": "ab",
            "nutr-useless_2": "cd",
            "nutr-useless_3": "ef",
            "nutr-useless_4": 1.23,
            "nutr-useless_5": 1.23,
            "nutr-useless_6": 123,
    }

}
