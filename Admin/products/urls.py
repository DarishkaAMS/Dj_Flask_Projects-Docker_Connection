from django.urls import path

from .views import ProductViewSet

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list_view',
        'post': 'create_view'
    })),
    path('products/<int:pk>', ProductViewSet.as_view({
        'get': 'retrieve_view',
        'put': 'update_view',
        'delete': 'delete_view',
    }))
]
