from django.shortcuts import render
from rest_framework import viewsets
from .serializers import InvoiceSerializer
from .models import Invoice

# Create your views here.
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all().order_by('created_on')
    serializer_class = InvoiceSerializer



