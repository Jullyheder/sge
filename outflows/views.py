from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView
)
from outflows.models import Outflow
from outflows.forms import OutflowForm


class OutflowListView(ListView):
    model = Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')
        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset


class OutflowCreateView(CreateView):
    model = Outflow
    template_name = 'outflow_create.html'
    form_class = OutflowForm
    success_url = reverse_lazy('outflow_list')

    def form_valid(self, form):
        outflow = form.save(commit=False)
        outflow.user_created = self.request.user
        outflow.user_updated = self.request.user
        return super().form_valid(form)


class OutflowDetailView(DetailView):
    model = Outflow
    template_name = 'outflow_detail.html'
    context_object_name = 'outflow'


class OutflowUpdateView(UpdateView):
    model = Outflow
    template_name = 'outflow_update.html'
    form_class = OutflowForm
    success_url = reverse_lazy('outflow_list')

    def form_valid(self, form):
        outflow = form.save(commit=False)
        outflow.user_updated = self.request.user
        return super().form_valid(form)
