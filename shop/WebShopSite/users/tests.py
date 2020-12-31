from django.test import TestCase
from .models import Tovar, Category,Adress, Country,City, Order
from django.contrib.auth.models import User
# Create your tests here.
class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(
            name="Мед"
        )
        Category.objects.create(
            name="Растение"
        )

    def test_Category_get_name_will_pass(self):
        honey = Category.objects.get(name="Мед")
        self.assertEqual(honey.__str__(), 'Мед')

    def test_Category_get_name_will_fail(self):
        plant = Category.objects.get(name="Растение")
        self.assertEqual(plant.__str__(), 'НЕ растение!')


class TovarTestCase(TestCase):
    def setUp(self):
        Category.objects.create(
            name="test_category"
        )
        test_category = Category.objects.get(name="test_category")
        Tovar.objects.create(
            name = "test_tovar",
            short_description = "Test description",
            full_description = "Test description",
            price=200,
            slug="test1",
            category=test_category,
        )

    def test_Tovar_get_name(self):
            test_tovar = Tovar.objects.get(slug="test1")
            self.assertEqual(test_tovar.__str__(), 'test_tovar')


