from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Product 
from .serializers import ProductSerializer, ProductCreateSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateView(generics.CreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
