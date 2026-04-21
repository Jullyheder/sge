from django.urls import path
from outflows.views import (
    OutflowListView,
    OutflowCreateView,
    OutflowDetailView
)


urlpatterns = [
    path('', OutflowListView.as_view(), name='outflow_list'),
    path('create/', OutflowCreateView.as_view(), name='outflow_create'),
    path('<int:pk>/detail/', OutflowDetailView.as_view(), name='outflow_detail'),
]
