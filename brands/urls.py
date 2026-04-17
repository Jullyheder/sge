from django.urls import path
from brands.views import (
    BrandListView,
    BrandCreateView,
    BrandDetailView,
    BrandUpdateView,
    BrandDeleteView
)


urlpatterns = [
    path('list/', BrandListView.as_view(), name='brand_list'),
    path('create/', BrandCreateView.as_view(), name='brand_create'),
    path('<int:pk>/detail/', BrandDetailView.as_view(), name='brand_detail'),
    path('<int:pk>/update/', BrandUpdateView.as_view(), name='brand_update'),
    path('<int:pk>/delete/', BrandDeleteView.as_view(), name='brand_delete'),
]
