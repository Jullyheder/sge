from django.urls import path
from suppliers.views import (
    SupplierListView,
    SupplierCreateView,
    SupplierDetailView,
    SupplierUpdateView,
    SupplierDeleteView
)


urlpatterns = [
    path('', SupplierListView.as_view(), name='supplier_list'),
    path('create/', SupplierCreateView.as_view(), name='supplier_create'),
    path('<int:pk>/detail/', SupplierDetailView.as_view(), name='supplier_detail'),
    path('<int:pk>/update/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier_delete'),
]
