from django.db import models

# Create your models here.
class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

class Runner(models.Model):
    MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')   
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)

class Manufacturer(models.Model):
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

class Topping(models.Model):
    pass

class Pizza(models.Model):
    topping = models.ManyToManyField(Topping)

class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ['horn_length']
        verbose_name_plural = 'oxen'