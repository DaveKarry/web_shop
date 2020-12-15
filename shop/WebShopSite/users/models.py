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

class Tovar(models.Model):
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=50)
    count = models.IntegerField()
    short_description = models.CharField(max_length=100)
    full_description = models.CharField(max_length=500)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=5)
    creation_time = models.DateTimeField(blank=True,null=False)
    slug = models.ImageField()


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

class OrderItem(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True,null=True)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Tovar, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.item.name} в количестве {self.quantity}"



class Order(models.Model):
    check = models.CharField(max_length=30)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField()
    tovars = models.ManyToManyField(OrderItem)

    def __str__(self):
        return self.user.username

    def create(self, user,status):
        self.user = user
        self.status = status
        self.check = "none"
        self.is_ordered = False
        self.save()

class Adress(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    index = models.CharField(max_length=50)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        adress = self.country+self.city+self.street+ self.number
        return adress