from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView
)
from inflows.models import Inflow
from inflows.forms import InflowForm


class InflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10
    permission_required = 'inflows.view_inflow'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_name = self.request.GET.get('search_name')
        if search_name:
            queryset = queryset.filter(
                Q(product__title__icontains=search_name)
                | Q(supplier__name__icontains=search_name)
            )

        return queryset


class InflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Inflow
    template_name = 'inflow_create.html'
    form_class = InflowForm
    success_url = reverse_lazy('inflow_list')
    permission_required = 'inflows.add_inflow'

    def form_valid(self, form):
        inflow = form.save(commit=False)
        inflow.user_created = self.request.user
        inflow.user_updated = self.request.user
        return super().form_valid(form)


class InflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Inflow
    template_name = 'inflow_detail.html'
    context_object_name = 'inflow'
    permission_required = 'inflows.view_inflow'
