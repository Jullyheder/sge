from django.urls import path
from brands.views import (
    BrandListView, BrandCreateView, BrandDetailView,
    BrandUpdateView, BrandDeleteView,
    BrandListCreateAPIView, BrandRetrieveUpdateDestroyAPIView
)


urlpatterns = [
    path('', BrandListView.as_view(), name='brand_list'),
    path('create/', BrandCreateView.as_view(), name='brand_create'),
    path('<int:pk>/detail/', BrandDetailView.as_view(), name='brand_detail'),
    path('<int:pk>/update/', BrandUpdateView.as_view(), name='brand_update'),
    path('<int:pk>/delete/', BrandDeleteView.as_view(), name='brand_delete'),

    path('api/v1/', BrandListCreateAPIView.as_view(), name='brand_list_create_api_view'),
    path(
        '<int:pk>/api/v1/',
        BrandRetrieveUpdateDestroyAPIView.as_view(),
        name='brand_retrieve_update_destroy_api_view'
    ),
]
