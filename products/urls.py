from django.urls import path
from .views import ProductViewSet

urlpatterns =[
    path('products', ProductViewSet.as_view({
        'get':'product_list_view',
        'post':'product_create_view'
    })),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'product_retrieve_view',
        'put': 'product_update_view',
        'delete': 'product_delete_view',
    })),
]