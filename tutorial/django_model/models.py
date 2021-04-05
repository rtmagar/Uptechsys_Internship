from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.TextField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    

class Sku(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True,)
    COLORS = (
        ('B', 'Black'),
        ('W', 'White'),
        ('G', 'Grey'),
    )
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    brand = models.CharField(max_length=20)
    color = models.CharField(max_length=15, choices=COLORS)
    size = models.CharField(max_length=1, choices=SIZES)

    def __str__(self):
        return self.brand

class Batch(models.Model):
    sku = models.OneToOneField(Sku, on_delete=models.CASCADE, primary_key=True,)
    quantity = models.IntegerField()
    country = models.CharField(max_length=15)
    shipping_date = models.DateField()
    manufacture_date = models.DateField()
    expiry_date = models.DateField()

    class Meta:
        db_table = 'Batch'
        ordering = ['country']

    def __str__(self):
        return self.country
