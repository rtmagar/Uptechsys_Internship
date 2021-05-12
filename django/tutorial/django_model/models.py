from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
class Base(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(MPTTModel, Base):
    name = models.CharField(max_length=15)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name

# class SubCategory(MPTTModel, Base):
#     name = models.CharField(max_length=15)

#     class Meta:
#         db_table = 'subcategory'
#         verbose_name_plural = 'subcategories'
#         ordering = ['name']
    
#     def __str__(self):
#         return self.name


class Product(Base):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=31)
    price = models.IntegerField()
    description = models.TextField()
    manufactured_date = models.DateField()
    expiry_date = models.DateField()

    class Meta:
        db_table = 'product'
        ordering = ['name']
    
    def __str__(self):
        return self.name

    
class Sku(Base):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
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
    brand = models.CharField(max_length=15)
    color = models.CharField(max_length=1, choices=COLORS)
    size = models.CharField(max_length=1, choices=SIZES)

    class Meta:
        db_table = 'sku'

    def __str__(self):
        return self.product.name

class Batch(Base):
    sku = models.ForeignKey(Sku, on_delete=models.CASCADE)
    batch_number = models.CharField(max_length=31)
    quantity = models.IntegerField()
    shipped_date = models.DateField()
    packed_date = models.DateField()
    
    
    class Meta:
        db_table = 'batch'
        verbose_name_plural = 'Batches'
        ordering = ['shipped_date']

    def __str__(self):
        return self.batch_number