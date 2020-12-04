from django.db import models

class FoodCategory(models.Model):
    category_name = models.CharField(max_length=300, unique=True)
    def __str__(self):
        return self.category_name

class FoodProduct(models.Model):

    product_name = models.CharField(max_length=300)
    nutriscore = models.CharField(max_length=1)
    barcode = models.PositiveBigIntegerField(unique=True)
    image_url = models.URLField(max_length=300)
    energy_kj = models.CharField(max_length=20)
    energy_kcal = models.CharField(max_length=20)
    protein = models.CharField(max_length=20)
    glucid = models.CharField(max_length=20)
    lipid = models.CharField(max_length=20)
    fiber = models.CharField(max_length=20)
    salt = models.CharField(max_length=20)

    categories = models.ManyToManyField(FoodCategory)

    def __str__(self):
        return self.product_name
