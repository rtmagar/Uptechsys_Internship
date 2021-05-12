from rest_framework import serializers
from .models import Invoice

class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = ('order', 'payment_choices', 'created_on', 'updated_on')

