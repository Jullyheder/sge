from django.urls import path
from inflows.views import (
    InflowListView, InflowCreateView, InflowDetailView,
    InflowListCreateAPIView, InflowRetrieveAPIView
)


urlpatterns = [
    path('', InflowListView.as_view(), name='inflow_list'),
    path('create/', InflowCreateView.as_view(), name='inflow_create'),
    path('<int:pk>/detail/', InflowDetailView.as_view(), name='inflow_detail'),

    path('api/v1/', InflowListCreateAPIView.as_view(), name='inflow_list_create_api_view'),
    path('<int:pk>/api/v1/', InflowRetrieveAPIView.as_view(), name='inflow_retrieve_api_view'),
]
