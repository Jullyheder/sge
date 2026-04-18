from django.urls import path
from inflows.views import (
    InflowListView,
    InflowCreateView,
    InflowDetailView,
    InflowUpdateView,
)


urlpatterns = [
    path('', InflowListView.as_view(), name='inflow_list'),
    path('create/', InflowCreateView.as_view(), name='inflow_create'),
    path('<int:pk>/detail/', InflowDetailView.as_view(), name='inflow_detail'),
    path('<int:pk>/update/', InflowUpdateView.as_view(), name='inflow_update')
]
