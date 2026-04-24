from django.urls import path
from suppliers.views import (
    SupplierListView, SupplierCreateView, SupplierDetailView,
    SupplierUpdateView, SupplierDeleteView,
    SupplierListCreateAPIView, SupplierRetrieveUpdateDestroyAPIView
)


urlpatterns = [
    path('', SupplierListView.as_view(), name='supplier_list'),
    path('create/', SupplierCreateView.as_view(), name='supplier_create'),
    path('<int:pk>/detail/', SupplierDetailView.as_view(), name='supplier_detail'),
    path('<int:pk>/update/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier_delete'),

    path('api/v1/', SupplierListCreateAPIView.as_view(), name='supplier_list_create_api_view'),
    path(
        '<int:pk>/api/v1/',
        SupplierRetrieveUpdateDestroyAPIView.as_view(),
        name='supplier_retrieve_update_destroy_api_view'
    ),
]
