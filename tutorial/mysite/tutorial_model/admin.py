from django.contrib import admin
from .models import Person, Runner, Manufacturer, Car, Topping, Pizza, Ox

# Register your models here.
admin.site.register(Person)
admin.site.register(Runner)
admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Ox)
