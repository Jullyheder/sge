from django.urls import path
from products.views import (
    ProductListView, ProductCreateView, ProductDetailView,
    ProductUpdateView, ProductDeleteView,
    ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView,
)


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/detail/', ProductDetailView.as_view(), name='product_detail'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('api/v1/', ProductListCreateAPIView.as_view(), name='product_list_create_api_view'),
    path(
        '<int:pk>/api/v1/',
        ProductRetrieveUpdateDestroyAPIView.as_view(),
        name='product_retrieve_update_destroy_api_view'
    ),
]
