from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from brands.models import Brand
from brands.forms import BrandForm


class BrandListView(ListView):
    model = Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class BrandCreateView(CreateView):
    model = Brand
    template_name = 'brand_create.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand_list')

    def form_valid(self, form):
        brand = form.save(commit=False)
        brand.user_created = self.request.user
        brand.user_updated = self.request.user
        return super().form_valid(form)


class BrandDetailView(DetailView):
    model = Brand
    template_name = 'brand_detail.html'
    context_object_name = 'brand'


class BrandUpdateView(UpdateView):
    model = Brand
    template_name = 'brand_update.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand_list')

    def form_valid(self, form):
        brand = form.save(commit=False)
        brand.user_updated = self.request.user
        return super().form_valid(form)


class BrandDeleteView(DeleteView):
    model = Brand
    template_name = 'brand_delete.html'
    context_object_name = 'brand'
    success_url = reverse_lazy('brand_list')
