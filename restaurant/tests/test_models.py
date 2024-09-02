from django.contrib.auth import get_user_model
from django.test import TestCase

from restaurant.models import DishType, Cook, Dish


class ModelTestCase(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name='Dish Type',
        )
        self.assertEqual(str(dish_type), f"{dish_type.name}")

    def test_cook_str(self):
        cook = Cook.objects.create(
            username="test_username",
            first_name="test_first_name",
            last_name="test_last_name",
        )
        self.assertEqual(str(cook), f"{cook.username} ({cook.first_name} {cook.last_name})")

    def test_cook_years_of_experience(self):
        years_of_experience = 1
        password = "Test12325d"
        username = "test_username"
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience,
        )
        self.assertEqual(cook.years_of_experience, years_of_experience)
        self.assertEqual(cook.username, username)
        self.assertTrue(cook.check_password(password))

    def test_dish_str(self):
        dish_type = DishType.objects.create(name='test_name')
        dish = Dish.objects.create(
            name="test_name",
            dish_type=dish_type,
            price=10,
        )
        self.assertEqual(str(dish), f"{dish.name} ({dish_type.name})")

