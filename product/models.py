from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=50)
    color_code = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=50, unique = True)
    size_code = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique = True)
    image = models.CharField(max_length=255)
    is_active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    image1 = models.CharField(max_length=500)
    image2 = models.CharField(max_length=500)
    image3 = models.CharField(max_length=500)
    image4 = models.CharField(max_length=500)
    sku = models.CharField(max_length=20, unique  = True, primary_key = True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    tag = models.CharField(max_length=255)
    is_stock = models.BooleanField(default = False) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    reviews = models.IntegerField()
    color = models.ManyToManyField(Color)
    size = models.ManyToManyField(Size)



