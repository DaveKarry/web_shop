from django.test import TestCase
from .models import Tovar, Category
# Create your tests here.
class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(
            name="Мед"
        )
        Category.objects.create(
            name="Растение"
        )

    def test_get_name(self):
        honey = Category.objects.get(name="Мед")
        plant = Category.objects.get(name="Растение")
        self.assertEqual(honey.__str__(), 'Мед')
        self.assertEqual(plant.__str__(), 'НЕ растение!')
