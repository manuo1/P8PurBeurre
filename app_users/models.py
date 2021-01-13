from django.db import models
from django.contrib.auth.models import AbstractUser
from app_products.models import FoodProduct


class UsersManager(models.Manager):
    def get_favorites_list(self, user):
        current_user_favorites_list = user.favorites.all()
        return current_user_favorites_list

    def add_to_favorites_list(self, user, product):
        user.favorites.add(product)


class User(AbstractUser):
    favorites = models.ManyToManyField(FoodProduct)
