from django.db import models

# Create your models here.
class Base(models.Model):
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Invoice(Base):
    CHOICES = [
        ('COD', 'Cash On Delivery'),
        ('PGT', 'Payment Gateway')
    ]
    order = models.IntegerField()
    payment_choices = models.CharField(max_length=3, choices=CHOICES)

    class Meta:
        db_table = 'payment_info'
        ordering = ['created_on']
        verbose_name = 'payment'
    
    def __str__(self):
        return self.payment_choices