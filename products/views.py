from rest_framework import viewsets

# Create your views here.


class ProductViewSet(viewsets.ViewSet):
    def product_list_view(self, request):
        pass

    def product_create_view(self, request):
        pass

    def product_retrieve_view(self, request, pk=None):
        pass

    def product_update_view(self, pk=None):
        pass

    def product_delete_view(self, request, pk=None):
        pass