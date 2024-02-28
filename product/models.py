from django.db import models

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
    image = models.JSONField(default = list)
    sku = models.CharField(max_length=20, unique  = True, primary_key = True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    tag = models.JSONField(default = list)
    is_stock = models.BooleanField(default = False) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    reviews = models.IntegerField()
    color = models.JSONField(default = list)
    size = models.JSONField(default = list)





