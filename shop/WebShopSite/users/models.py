from django.utils import timezone
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tovar(models.Model):
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=50)
    count = models.IntegerField()
    short_description = models.CharField(max_length=100)
    full_description = models.CharField(max_length=500)
    price = models.FloatField()
    category = models.ManyToManyField(Category)
    creation_time = models.DateTimeField(blank=True,null=False)

    def __str__(self):
        return self.name

    def create(self):
        self.creation_time = timezone.now()
        self.save()


class Users_purchase(models.Model):
    check = models.CharField(max_length=30)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    status = models.ForeignKey('status', on_delete=models.CASCADE)
    def __str__(self):
        str = self.user.username + " "+self.status.name
        return str

    def create(self, user,status):
        self.user = user
        self.status = status
        self.check = "none"
        self.save()


class Status(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return  self.name

class Tovars_in_purchase(models.Model):
    users_purchase = models.ForeignKey('Users_purchase', on_delete=models.CASCADE)
    tovar = models.ForeignKey('Tovar',on_delete=models.CASCADE)
    count = models.IntegerField()

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