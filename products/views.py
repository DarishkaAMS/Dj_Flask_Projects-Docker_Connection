from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

# Create your views here.


class ProductViewSet(viewsets.ViewSet):

    def product_list_view(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def product_create_view(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def product_retrieve_view(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def product_update_view(self, pk=None):
        pass

    def product_delete_view(self, request, pk=None):
        pass
