from rest_framework import viewsets
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
        pass

    def product_retrieve_view(self, request, pk=None):
        pass

    def product_update_view(self, pk=None):
        pass

    def product_delete_view(self, request, pk=None):
        pass