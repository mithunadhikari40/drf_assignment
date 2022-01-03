from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Product
from .serializer import ProductSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
