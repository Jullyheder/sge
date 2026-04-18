from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView
)
from inflows.models import Inflow
from inflows.forms import InflowForm


class InflowListView(ListView):
    model = Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_name = self.request.GET.get('search_name')
        if search_name:
            queryset = queryset.filter(
                Q(product__title__icontains=search_name)
                | Q(supplier__name__icontains=search_name)
            )

        return queryset


class InflowCreateView(CreateView):
    model = Inflow
    template_name = 'inflow_create.html'
    form_class = InflowForm
    success_url = reverse_lazy('inflow_list')

    def form_valid(self, form):
        inflow = form.save(commit=False)
        inflow.user_created = self.request.user
        inflow.user_updated = self.request.user
        return super().form_valid(form)


class InflowDetailView(DetailView):
    model = Inflow
    template_name = 'inflow_detail.html'
    context_object_name = 'inflow'


class InflowUpdateView(UpdateView):
    model = Inflow
    template_name = 'inflow_update.html'
    form_class = InflowForm
    success_url = reverse_lazy('inflow_list')

    def form_valid(self, form):
        inflow = form.save(commit=False)
        inflow.user_updated = self.request.user
        return super().form_valid(form)
