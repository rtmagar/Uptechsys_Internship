from django.contrib import admin
from .models import Product, Sku, Batch, Category
from mptt.admin import MPTTModelAdmin
# Register your models here.
admin.site.register(Category, MPTTModelAdmin)
# admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Sku)
admin.site.register(Batch)

