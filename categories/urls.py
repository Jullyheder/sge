from django.urls import path
from categories.views import (
    CategoryListView, CategoryCreateView, CategoryDetailView,
    CategoryUpdateView, CategoryDeleteView,
    CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView
)


urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('create/', CategoryCreateView.as_view(), name='category_create'),
    path('<int:pk>/detail/', CategoryDetailView.as_view(), name='category_detail'),
    path('<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    path('api/v1/', CategoryListCreateAPIView.as_view(), name='category_list_create_api_view'),
    path(
        '<int:pk>/api/v1/',
        CategoryRetrieveUpdateDestroyAPIView.as_view(),
        name='category_retrieve_update_destroy_api_view'
    ),
]
