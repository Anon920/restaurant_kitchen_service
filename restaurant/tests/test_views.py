from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from restaurant.models import DishType

DISH_TYPE_URL = reverse("restaurant:dish-type-list")


class PublicDishTypeTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(DISH_TYPE_URL)
        self.assertEqual(res.status_code, 200)


class PrivateDishTypeTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='<PASSWORD>',
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_type(self):
        DishType.objects.create(name="test_dish_type")
        res = self.client.get(DISH_TYPE_URL)
        self.assertEqual(res.status_code, 200)
        dish_type_all = DishType.objects.all()
        self.assertEqual(
            list(res.context["dish_type_list"]), list(dish_type_all)
        )
        self.assertTemplateUsed(res, "restaurant/dish_type_list.html")
