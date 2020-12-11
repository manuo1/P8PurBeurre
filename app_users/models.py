from django.db import models
from django.contrib.auth.models import AbstractUser
from app_products.models import FoodProduct

class User(AbstractUser):
    favorites = models.ManyToManyField(FoodProduct)
