from django.urls import path
from outflows.views import (
    OutflowListView,
    OutflowCreateView,
    OutflowDetailView,
    OutflowUpdateView
)


urlpatterns = [
    path('', OutflowListView.as_view(), name='outflow_list'),
    path('create/', OutflowCreateView.as_view(), name='outflow_create'),
    path('<int:pk>/detail/', OutflowDetailView.as_view(), name='outflow_detail'),
    path('<int:pk>/update/', OutflowUpdateView.as_view(), name='outflow_update')
]
