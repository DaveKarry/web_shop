from django.utils import timezone
from django.db import models
from django.shortcuts import reverse
# Create your models here.

CATEGORY_CHOICES = (
    ('Milk', 'Молочная продукция'),
    ('Honey', 'Мёд'),
    ('Meat', 'Мясо'),
    ('Egg', 'Яйца птицы'),
    ('Plant', 'Растительный продукт'),
)
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Tovar(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images')
    short_description = models.CharField(max_length=100)
    full_description = models.CharField(max_length=500)
    price = models.FloatField()
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def create(self):
        self.creation_time = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("tovar", kwargs ={
            'slug': self.slug
        })

    def get_add_to_order_url(self):
        return reverse("add-to-order", kwargs ={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={
            'slug': self.slug
        })

    def get_delete_tovar_url(self):
        return reverse("delete", kwargs={
            'slug': self.slug
        })
    def get_add_image_url(self):
        return reverse("add_image", kwargs={
            'slug': self.slug
        })



class OrderItem(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True,null=True)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Tovar, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.item.name} в количестве {self.quantity}"

    def get_total_item_price(self):
        return self.quantity * self.item.price


class Order(models.Model):
    pdf_check = models.FileField(null=True, default=1)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField()
    tovars = models.ManyToManyField(OrderItem)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.tovars.all():
            total+=order_item.get_total_item_price()
        return total

class Country(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
            return self.name

class Adress(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    index = models.CharField(max_length=50)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        adress = self.country+" "+self.city+" "+self.street+" "+self.number
        return adress

