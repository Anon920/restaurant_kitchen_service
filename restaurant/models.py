from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from restaurant_kitchen_service import settings


class DishType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(default=0)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cooks = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="dishes"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.dish_type})"
