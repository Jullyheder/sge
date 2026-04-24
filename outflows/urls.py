from django.urls import path
from outflows.views import (
    OutflowListView, OutflowCreateView, OutflowDetailView,
    OutflowListCreateAPIView, OutflowRetrieveAPIView
)


urlpatterns = [
    path('', OutflowListView.as_view(), name='outflow_list'),
    path('create/', OutflowCreateView.as_view(), name='outflow_create'),
    path('<int:pk>/detail/', OutflowDetailView.as_view(), name='outflow_detail'),

    path('api/v1/', OutflowListCreateAPIView.as_view(), name='outflow_list_create_api_view'),
    path('<int:pk>/api/v1/', OutflowRetrieveAPIView.as_view(), name='outflow_retrieve_api_view'),
]
